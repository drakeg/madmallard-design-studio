#[tauri::command]
fn create_document(name: String) -> String {
    design_document::Document::new(name).to_json().expect("document serializes")
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![create_document])
        .run(tauri::generate_context!())
        .expect("error while running application");
}
