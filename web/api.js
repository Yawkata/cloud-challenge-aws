const API_BASE_URL = "https://ayoojw0ev5.execute-api.eu-north-1.amazonaws.com/test";

export async function getVisitorCount() {
    const response = await fetch(`${API_BASE_URL}/visitor`);
    const data = await response.json();
    return data.visitor_count;
}

export async function incrementVisitorCount() {
    const response = await fetch(`${API_BASE_URL}/visitor`, {
        method: "POST"
    });
    const data = await response.json();
    return data.visitor_count;
}
