function fetchFeedbackData() {
    fetch('/api/method/library_management.library_management.doctype.customer_feedback.customer_feedback.get_data')
        .then(response => response.json())
        .then(r => {
            if (r.message && r.message.length > 0) {
                displayPatientData(r.message);
            } else {
                document.getElementById("result").innerHTML = "<p>No feedback data found.</p>";
            }
        })
        .catch(err => {
            console.error("Error fetching feedback data:", err);
            document.getElementById("result").innerHTML = "<p style='color: red;'>Failed to load data.</p>";
        });
}


function displayPatientData(data) {
    const keys = Object.keys(data[0]);

    let html = `<table style="width: 100%; border-collapse: collapse; font-family: Arial, sans-serif;">
        <thead>
            <tr style="background-color: #f2f2f2;">`;

    keys.forEach(key => {
        html += `<th style="padding: 10px; border: 1px solid #ccc;">${key}</th>`;
    });

    html += `</tr></thead><tbody>`;

    data.forEach(row => {
        html += `<tr>`;
        keys.forEach(key => {
            html += `<td style="padding: 10px; border: 1px solid #ccc;">${row[key] || 'N/A'}</td>`;
        });
        html += `</tr>`;
    });

    html += `</tbody></table>`;
    document.getElementById("result").innerHTML = html;
}
