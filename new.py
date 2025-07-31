a = """```json
{
  "profile_summary": "Data Analyst with 2+ years of experience in analyzing data, building dashboards, and delivering actionable insights. Proficient in SQL, Python (Pandas, NumPy, Matplotlib, Seaborn), and Excel. Adept at translating business needs into data questions and presenting findings to stakeholders. Seeking to leverage expertise in data analysis to contribute to data-driven decision-making at LumaMetrics.",
  "functional_areas": [
    "Data Analysis",
    "Data Visualization",
    "Business Intelligence",
    "SQL Development",
    "ETL Processes",
    "Statistical Analysis"
  ],
  "technical_skills": [
    "SQL (Joins, CTEs, Window Functions)",
    "Python (Pandas, NumPy, Matplotlib, Seaborn)",
    "Data Visualization (Tableau, Power BI)",
    "Advanced Excel (Pivot Tables, Charts, Lookups, Power Query, Power Pivot)",
    "ETL Processes"
  ],
  "project1_title": "Inventory Management System with QR Code Tracking",
  "project1_duration": "12/2024 – 01/2025",
  "project1_points": [
    "Developed a system to track 1000+ products using QR scanning, improving inventory management efficiency.",
    "Utilized data analysis techniques to identify trends in product movement and optimize stock levels.",
    "Created reports and visualizations to provide insights into inventory performance.",
    "Leveraged Excel for data analysis and reporting."
  ],
  "project2_title": "AI-Powered Smart Classroom Automation",
  "project2_duration": "06/2024 – 12/2024",
  "project2_points": [
    "Automated attendance for 200+ students using InsightFace, saving 20+ hours/month and improving data accuracy.",
    "Employed Python and machine learning libraries to develop and implement the automation system.",
    "Designed and implemented a data pipeline to collect and process attendance data.",
    "Contributed to improved classroom management through data-driven automation."
  ]
}
```"""[8:-3]
print(a)
print(type(eval(a)))