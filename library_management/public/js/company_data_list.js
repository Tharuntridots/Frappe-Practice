frappe.listview_settings['Company Data'] = {
    get_chart_data: function(columns, data) {
        const status_count = {};

        // Count each status
        data.forEach(row => {
            const status = row.status || "Unknown";
            if (!status_count[status]) {
                status_count[status] = 0;
            }
            status_count[status]++;
        });

        return {
            data: {
                labels: Object.keys(status_count),
                datasets: [
                    {
                        name: "Status Count",
                        values: Object.values(status_count)
                    }
                ]
            },
            type: 'pie' // or 'donut'
        };
    }
};
