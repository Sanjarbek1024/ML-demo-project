async function classifyNews() {
    const text = document.getElementById("newsText").value;
    const resultDiv = document.getElementById("result");

    if (!text.trim()) {
        resultDiv.innerHTML = "⚠️ Please enter some text first!";
        return;
    }

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text })
        });

        const data = await response.json();
        resultDiv.innerHTML = `✅ Predicted Category: <b>${data.category}</b>`;
    } catch (error) {
        resultDiv.innerHTML = "❌ Error: Could not classify.";
        console.error(error);
    }
}
