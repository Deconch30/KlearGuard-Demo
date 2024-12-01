document.getElementById("demoForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    const email = document.getElementById("email").value;
    const userText = document.getElementById("userText").value;

    fetch("/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email: email, text: userText })
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById("result");
        resultDiv.innerHTML = `
            <p>Compliance Status: ${data.compliance_status}</p>
            <p>Bias Detected: ${data.bias_detected ? "Yes" : "No"}</p>
            <p>Sentiment Score: ${data.sentiment_score.compound}</p>
        `;
    })
    .catch(error => {
        console.error("Error:", error);
    });
});
