document.getElementById("studentForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const data = {
        attendance_rate: Number(document.getElementById("attendance").value),
        average_grade: Number(document.getElementById("grade").value),
        study_hours_per_week: Number(document.getElementById("hours").value),
        engagement_score: Number(document.getElementById("engagement").value),
        previous_failures: Number(document.getElementById("failures").value)
    };

    const response = await fetch("http://127.0.0.1:8000/recommend", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();

    let output = `<h3>Status: ${result.risk_status}</h3><ul>`;
    result.recommended_resources.forEach(r => {
        output += `<li>${r}</li>`;
    });
    output += "</ul>";

    document.getElementById("result").innerHTML = output;
});
