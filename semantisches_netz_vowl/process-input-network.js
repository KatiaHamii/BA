const fs = require("fs");
const json = require("./input-network.json");

let outputObject = {
  nodes: [],
  links: [],
};

const rootWord = Object.keys(json)[0];

const processObject = (obj, parentNode = null) => {
  Object.keys(obj).forEach((key) => {
    let nodeForWord = outputObject.nodes.find((n) => n.word === key);

    if (!nodeForWord) {
      nodeForWord = {
        id: outputObject.nodes.length,
        word: key,
        parentId: parentNode.id,
      };

      outputObject.nodes.push(nodeForWord);
    }

    outputObject.links.push({
      from: parentNode.id,
      to: nodeForWord.id,
    });

    if (typeof obj[key] === "object") {
      processObject(obj[key], nodeForWord);
    }
  });
};

const rootNode = {
  id: 0,
  word: rootWord,
};

outputObject.nodes.push(rootNode);

processObject(json[rootWord], rootNode);

fs.writeFileSync("./processed-input-network.json", JSON.stringify(outputObject), (err) => {
  if (err) {
    console.error(err);
  }
});
