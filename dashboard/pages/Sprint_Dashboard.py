import streamlit as st

from api_client import (
    get_sprint_metrics, 
    get_sprint_readiness, 
    get_sprint_risk, 
    download_sprint_report, 
    get_sprint_capacity, 
    get_workload
)

from utils import (
    page_header
)

from components.metrics import (
    show_metrics
)

from components.charts import (
    status_chart,
    story_point_chart, 
    priority_chart
)

page_header(
    "📊 Sprint Dashboard",
    "Sprint Overview"
)

tickets = get_sprint_metrics()
all_tickets = tickets

st.subheader(
    "Filters"
)

col1, col2 = st.columns(2)
with col1:
    selected_status = st.selectbox(
        "Status",
        [
            "All",
            "To Do",
            "In Progress",
            "Done"
        ]
    )

with col2:
    selected_priority = st.selectbox(
        "Priority",
        [
            "All",
            "Highest",
            "High",
            "Medium",
            "Low"
        ]
    )
    
filtered_tickets = all_tickets
if selected_status != "All":
    filtered_tickets = [
        t
        for t in filtered_tickets
        if t["status"] == selected_status
    ]

if selected_priority != "All":
    filtered_tickets = [
        t
        for t in filtered_tickets
        if t["priority"] == selected_priority
    ]
    

if not filtered_tickets:
    st.warning(
        "No tickets found for selected filters."
    )
    
    st.stop()
    
      
show_metrics(
    filtered_tickets
)

st.divider()

status_chart(
    filtered_tickets
)

st.divider()

story_point_chart(
    filtered_tickets
)

st.divider()

priority_chart(
    filtered_tickets
)

st.divider()

st.subheader(
    "Highest Priority Tickets"
)

for ticket in filtered_tickets:
    if ticket["priority"] in [
        "High",
        "Highest"
    ]:

        st.write(
            f"#{ticket['id']} - {ticket['title']}"
        ) 
        
        
st.divider()

st.subheader(
    "🚀 Sprint Readiness Analysis"
)

if st.button(
    "Analyze Sprint Readiness",
    use_container_width=True
):

    with st.spinner(
        "Analyzing sprint..."
    ):

        readiness = get_sprint_readiness()

        st.markdown(
            readiness
        ) 
        
        
st.divider()

st.subheader(
    "⚠️ Sprint Risk Analysis"
)

if st.button(
    "Analyze Sprint Risks",
    use_container_width=True
):

    with st.spinner(
        "Analyzing sprint risks..."
    ):

        risk = get_sprint_risk()

        st.markdown(
            risk
        ) 
        
        
st.divider()

st.subheader(
    "📈 Sprint Capacity Analysis"
)

if st.button(
    "Analyze Sprint Capacity",
    use_container_width=True
):

    with st.spinner(
        "Analyzing capacity..."
    ):

        capacity = get_sprint_capacity()

        st.markdown(
            capacity
        )
        
st.divider() 

st.subheader(
    "👤 Team Workload"
)

if st.button(
    "Analyze Workload",
    use_container_width=True
):

    workload = get_workload()

    total = sum(
        workload.values()
    )

    average = (
        total / len(workload)
        if workload
        else 0
    )

    for assignee, points in workload.items():

        st.write(
            f"**{assignee}** : {points} SP"
        )

    st.divider()

    st.write(
        f"Average Load: {average:.1f} SP"
    )

    overloaded = []
    for assignee, points in workload.items():
        if points > average * 1.5:
            overloaded.append(
                assignee
            )

    if overloaded:
        st.warning(
            "Potentially overloaded: "
            + ", ".join(overloaded)
        )

    else:
        st.success(
            "Workload appears balanced."
        )
        
st.divider()

st.subheader(
    "📄 Export Sprint Report"
)

if st.button(
    "Generate Report",
    use_container_width=True
):

    with st.spinner(
        "Generating PDF..."
    ):

        pdf = download_sprint_report()

        st.download_button(
            label="Download PDF",
            data=pdf,
            file_name="sprint_report.pdf",
            mime="application/pdf"
        )