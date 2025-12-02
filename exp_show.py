import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
st.header("🛡️Risk Tracker")
st.set_page_config(layout="wide")
st.markdown("***🧠 Monitor employee financial risk and performance in one place.***")


@st.dialog("creation")
def get_emp():
    emp=st.number_input("enter id: ",min_value=1)
    name=st.text_input("enter name: ")
    salary=st.number_input("enter salary: ",min_value=1)
    expenses=st.number_input("enter expenses: ",min_value=1)
    attendance=st.number_input("enter attendance: ",min_value=1)
    performance=st.number_input("enter performance: ",min_value=1)
    btn=st.button("create employee")
    if btn:
        url=f"http://127.0.0.1:8000/emp?employee_id={emp}&name={name}&salary={salary}&expenses={expenses}&attendance={attendance}&performance={performance}"
        res1=requests.post(url)
        if res1.status_code==200:
            st.toast("emp created")
            st.rerun()

@st.dialog("deletion")
def del_emp():
    employee_id=st.number_input("enter id: ",min_value=1)
    btn=st.button("del employee")
    if btn:
        url=f"http://127.0.0.1:8000/emp/{employee_id}"
        res1=requests.delete(url)
        if res1.status_code==200:
            st.toast("emp deleted")
            st.rerun()



res=requests.get("http://127.0.0.1:8000/emp")
if res.status_code==200:
    res=res.json()
    df=pd.DataFrame(res,columns=["Employee_ID", "Name", "Salary", "Expenses", "Attendance", "Performance","Savings","Risk"])
    df = df.sort_values(by="Employee_ID")


    fold=st.sidebar.radio("Settings",["Employees","Risk Rate"],label_visibility='hidden')
    if fold == "Employees":
        st.sidebar.subheader("🧑‍💼All Employees")
        for emp in res:
            st.sidebar.write("-> ",emp[1])
    if fold == "Risk Rate":
        st.sidebar.subheader("🛑Risk Data")
        tab=st.sidebar.selectbox("",["High","Medium","Low"])
        if tab=="High":
            for emp in res:
                if emp[7]>60:
                 st.sidebar.write(str(emp[1])+" - "+str(emp[7]))                
        if tab=="Medium":
            for emp in res:
                if emp[7]>40 and emp[7]<=60:
                 st.sidebar.write(str(emp[1])+" - "+str(emp[7]))
        if tab=="Low":
            for emp in res:
                if emp[7]>0 and emp[7]<=40:
                 st.sidebar.write(str(emp[1])+" - "+str(emp[7]))

    

    tab=st.tabs(["🎯OverView","🔄Modification","💡Suggestions"])
##        ##   
##OVERVIEW##
##        ##
    with tab[0]:
        with st.container(border=True):
            col1,col2,col3,col4,col5=st.columns([1,1,1,1,1])
            col1.metric("Employees",len(df))
            col2.metric("Highest Salary",df["Salary"].max())
            col3.metric("Minimum Expenses",df["Expenses"].min())
            col4.metric("Highest Savings",df["Savings"].max())
            max_risk=res[0][7]
            name=res[0][1]
            for i in range(len(res)):
                if res[i][7]>max_risk:
                    max_risk=res[i][7]
                    name=res[i][1]
            col5.metric("High Risk Employee",name)
        st.subheader("📊Employee Risk Bar Graph")
        names = [emp[1] for emp in res]
        risks = [emp[7] for emp in res]

        fig, ax = plt.subplots()
        ax.bar(names, risks)

        ax.set_xlabel("Employees")
        ax.set_ylabel("Risk Score")

        plt.xticks(rotation=45)

        st.pyplot(fig)


    with tab[1]:
        col=st.columns([0.5,1,1,0.5])
        with col[1]:
         btn1=st.button("Create Employee",type='primary')
        with col[2]:
         btn5=st.button("Delete Employee",type='primary')
        st.dataframe(df,hide_index="True")

        if btn1:
            get_emp()

        if btn5:
            del_emp()
    
    with tab[2]:
        suggest=st.text_input("📝Suggest Employee",placeholder="Employee Id")
        url=f"http://127.0.0.1:8000/emp/{suggest}"
        res1=requests.get(url)
        if res1.status_code==200:
          res1=res1.json()
        #   st.write(res1)
          if res1 is None or suggest=="":
            st.error("No Employee Found")
            st.stop()             
          else:
            col=st.columns([1,1])
            with col[0]:
                with st.container(border=True):
                    st.write("Employee : ",res1[1])
                    st.write(f"Risk Score : {res1[7]}")
                    if res1[7]>60:
                            risk_level="High"             
                    elif res1[7]>40 and res1[7]<=60:
                            risk_level="Medium"             
                    elif res1[7]>=0 and res1[7]<=40:
                            risk_level="Low"             
                    st.write(f"Risk Level : {risk_level}")
                    if res1[7]<50 and res1[7]>=0:
                     st.markdown(f"Overall Status: ***Good Improvement***")
                    else:
                     st.markdown(f"Overall Status: ***Needs Improvement***")
                     
            with col[1]:
                with st.container(border=True):
                    st.write(f"Attendance - {res1[4]}% ")
                    st.write(f"Performance - {res1[5]}% ")
                    st.write(f"Savings - {res1[6]}/- ")
            if res1[4]<75:
                st.error("It should be Atleast 75%")
            else:
                 st.success("Your Have Good percent of Attendance!!")
            if res1[5]<70:
                st.error("Performance should be atleast 70%")
            else:
                st.success("Your Have Good percent of Performance!!")
            saving = res1[6]
            salary = res1[2]
            ten_percent = salary * 0.10
            twenty_percent = salary * 0.20
            if saving <= 0:
                st.error("You have no savings. Reduce expenses immediately.")
            elif saving < ten_percent:
                st.warning("Savings are too low. Try to save at least 10% of salary.")
            elif saving < twenty_percent:
                st.info("Savings are okay, but try to reach 20% of salary.")
            else:
                st.success("You have very good savings!")





