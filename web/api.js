const API_BASE_URL = "https://vi9ausvov7.execute-api.eu-north-1.amazonaws.com/test";

export async function incrementVisitorCount() {
    const response = await fetch(`${API_BASE_URL}/visitor`, {
        method: "POST"
    });
    const data = await response.json();
    return data.visitor_count;
}
