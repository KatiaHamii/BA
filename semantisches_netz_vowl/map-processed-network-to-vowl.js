const fs = require("fs");
const inputJson = require("./processed-network-with-synonyms.json");

let outputObject = {
  classes: [],
  classAttributes: [],
  properties: [],
  propertyAttributes: [],
};

const getHeader = () => {
  return {
    prefixList: {
      rdf: "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
      rdfs: "http://www.w3.org/2000/01/rdf-schema#",
      owl: "http://www.w3.org/2002/07/owl#",
      xsd: "http://www.w3.org/2001/XMLSchema#",
    },
  };
};

const getClass = (id) => {
  return {
    id: String(id),
    type: "owl:Class",
  };
};

const getClassAttribute = (id, label, type, synonyms) => {
  return {
    id: String(id),
    type: "owl:Class",
    label: label,
    attributes: type === "extern" ? ["external"] : undefined,
    comment:
      synonyms?.length > 0
        ? {
            en: synonyms.join(", "),
          }
        : undefined,
  };
};

let propertyCounter = 0;
const getProperty = () => {
  propertyCounter++;
  return {
    id: String(propertyCounter),
    type: "owl:objectProperty",
  };
};

const getPropertyAttribute = ({ propertyId, fromId, toId }) => {
  return {
    id: propertyId,
    range: toId,
    domain: fromId,
    attributes: ["object", "anonymous"],
  };
};

// add nodes to the output object
const populateClasses = (nodes) => {
  let classes = [];
  nodes.forEach((node) => {
    outputObject.classes.push(getClass(node.id));
    outputObject.classAttributes.push(
      getClassAttribute(node.id, node.word, node.type, node.synonyms)
    );
  });
};

// add connections between nodes to the output object
const populateProperties = (links) => {
  links.forEach((link) => {
    const property = getProperty();
    const propertyAttribute = getPropertyAttribute({
      propertyId: property.id,
      fromId: String(link.from),
      toId: String(link.to),
    });

    outputObject.properties.push(property);
    outputObject.propertyAttributes.push(propertyAttribute);
  });
};

const getVowlObj = (obj) => {
  const { nodes, links } = obj;
  populateClasses(nodes);
  populateProperties(links);

  const vowlObj = {
    header: getHeader(),
    class: outputObject.classes,
    classAttribute: outputObject.classAttributes,
    property: outputObject.properties,
    propertyAttribute: outputObject.propertyAttributes,
  };

  return vowlObj;
};

fs.writeFileSync(
  "./vowl-output.json",
  JSON.stringify(getVowlObj(inputJson)),
  (err) => {
    if (err) {
      console.error(err);
    }
  }
);
