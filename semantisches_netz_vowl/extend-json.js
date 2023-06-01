const fs = require("fs");
const inputJson = require("./processed-input-network.json");

const data = fs.readFileSync("./concepts-list-with-synonyms.csv", "utf8");

const lines = data.split("\n");

const inputWordsMap = inputJson.nodes.reduce((result, curNode, index) => {
  return {
    ...result,
    [curNode.word]: index,
  };
}, {});

const extendWord = (word, synonyms, wordForms, type) => {
  const index = inputWordsMap[word];

  if (!word || typeof index === "undefined") {
    word && console.log(word);
    return;
  }

  const originalNode = inputJson.nodes[index];

  inputJson.nodes[index] = {
    ...originalNode,
    type,
    synonyms,
    wordForms,
  };
};

lines.forEach((line) => {
  const [word, type, synonyms, wordForms] = line.split(";");

  const processedWord = word.trim();

  const processedSynonyms = (synonyms?.split(",") || [])
    .map((w) => (!!w ? w.trim() : ""))
    .filter(Boolean);
  const processedWordForms = (wordForms?.split(",") || [])
    .map((w) => (!!w ? w.trim() : ""))
    .filter(Boolean);

  extendWord(processedWord, processedSynonyms, processedWordForms, type);
});

fs.writeFileSync("./processed-network-with-synonyms.json", JSON.stringify(inputJson), (err) => {
  if (err) {
    console.error(err);
  }
});
