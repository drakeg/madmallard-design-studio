use serde::{Deserialize, Serialize};
use uuid::Uuid;

#[derive(Debug, Clone, PartialEq, Serialize, Deserialize)]
pub struct Document {
    pub schema_version: u32,
    pub id: Uuid,
    pub name: String,
    pub nodes: Vec<Node>,
}
#[derive(Debug, Clone, PartialEq, Serialize, Deserialize)]
pub struct Node {
    pub id: Uuid,
    pub name: String,
    pub x: f64,
    pub y: f64,
    pub width: f64,
    pub height: f64,
    pub kind: NodeKind,
}
#[derive(Debug, Clone, PartialEq, Serialize, Deserialize)]
#[serde(tag = "type", content = "data")]
pub enum NodeKind {
    Rectangle { fill: String },
    Ellipse { fill: String },
    Text { content: String, font_size: f64 },
}
impl Document {
    pub fn new(name: impl Into<String>) -> Self {
        Self {
            schema_version: 1,
            id: Uuid::new_v4(),
            name: name.into(),
            nodes: Vec::new(),
        }
    }
    pub fn add_node(&mut self, node: Node) {
        self.nodes.push(node);
    }
    pub fn to_json(&self) -> Result<String, serde_json::Error> {
        serde_json::to_string_pretty(self)
    }
    pub fn from_json(json: &str) -> Result<Self, serde_json::Error> {
        serde_json::from_str(json)
    }
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn document_round_trip() {
        let mut doc = Document::new("Test");
        doc.add_node(Node {
            id: Uuid::new_v4(),
            name: "Box".into(),
            x: 0.0,
            y: 0.0,
            width: 100.0,
            height: 80.0,
            kind: NodeKind::Rectangle {
                fill: "#FF0000".into(),
            },
        });
        assert_eq!(doc, Document::from_json(&doc.to_json().unwrap()).unwrap());
    }
}
