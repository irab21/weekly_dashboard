import numpy as np 
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from PIL import Image 
from plotly.subplots import make_subplots

password= st.text_input('Please Enter The Password')
if (password == ("Manpreet") or password==("Abhishek") or password ==("Deepa") or password==("Akanksha") or password==("Amitender") or password=="Ravleen" or password=="Talib" or password=="Chandra" or password=="Dilip" or password=="Soorabh"):
	
	image_url='posterityfinal.png'
	image= Image.open(image_url) 
	st.image(image,width=350)

	st.title('Weekly Score board')
	st.sidebar.title('Options ')
	st.markdown("### Your team's performance for the last week 📓" )
	st.write("This Dashboard is prepared to give you a better insight into your team's overall performance as well as give you an idea of where you stand in comparision to other  teams")

	DATA_URL= 'weekly_scoreboard.xlsx'

	def load_data():
		data=pd.read_excel(DATA_URL)

		return data 

	data = load_data()

	#st.write(data)
	

	teams= data['Team Name']
	team1=data['Team Name'].to_list()
	cv_target=data['CV target'].to_list()
	interview=data['Interviews'].to_list()
	cv_percent=data['CV Submission Percentage'].round(decimals=0).to_list()
	cv_conversion=data['CV Conversion'].round(decimals=0).to_list()
	cv_sr=data['CV Ratio Scale'].to_list()
	i_sr=data['Interview Ratio Scale'].round(decimals=3).to_list()
	final=data['Final Point Scale'].round(decimals=3).to_list()





	st.sidebar.subheader('Data Division')
	#select= st.sidebar.selectbox('Please select the category',['Absolute Numbers','Ratios'],key=1)

	#new data frame
	cv_submission=data['CV Submission'].to_list()


	#st.write(cv_submission)
	st.write('Hover Over the Graphs to see the numbers')
	if st.sidebar.checkbox('Show Number of CV Submission and Interviews', True, key=1):
		fig=go.Figure()
		fig.add_trace(go.Bar(x=team1,y=cv_target,name='CV Target',marker_color='indianred',text=cv_target))
		fig.add_trace(go.Bar(x=team1,y=cv_submission,name='CV Submitted', marker_color='darkviolet',text=cv_submission))
		fig.add_trace(go.Bar(x=team1,y=interview,name='Interviews',marker_color='darkolivegreen',text=interview))
		fig.update_traces(texttemplate='%{text:.5s}', textposition='outside',width=0.4)
		fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig.update_layout(barmode='group',height=600)
		st.plotly_chart(fig)




	st.sidebar.markdown('### Please select the graph you want to see')
	select= st.sidebar.selectbox('Drop Box',('CV Submission Percentage','CV Conversion Percentage'),key=2)
	if select=='CV Submission Percentage':
		st.write('### CV Submission Percentage is the Percentage of CV submission target achieved by the Team in the last week\n')
		st.write('\n\n')
		fig1=px.line(x=team1,y=cv_percent,text=cv_percent,hover_name=team1)
		fig1.update_traces(texttemplate='%{text:.2s}', textposition='top center')
		fig1.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		st.plotly_chart(fig1)



	else:
		st.write('### CV Conversion Percentage is the Percentage taken from the ratio of total number of Interviews and total number of CVs Submitted ')
		st.write('\n\n')
		fig2=px.line(x=team1,y=cv_conversion,text=cv_conversion)
		fig2.update_traces(texttemplate='%{text:.2s}', textposition='top center')
		st.plotly_chart(fig2)

	st.sidebar.markdown('### Scaled Ratio Score')
	if st.sidebar.checkbox('CV Ratio Scale',True,key=4):
		st.write('### CV Ratio Scale is the ratio of cv submitted to the cv submission target scaled ')
		fig3=px.line(x=team1,y=cv_sr,text=cv_sr)
		fig3.update_traces(texttemplate='%{text:.2s}',textposition='top center')
		st.plotly_chart(fig3)
	if st.sidebar.checkbox('Interview Ratio Scale',True,key=5):
		st.write('### Interview Ratio scale is a scaled ratio of Total Number of Interviews to the Total Number of CV Submitted')
		st.write('\n\n')
		fig4=px.line(x=team1,y=i_sr,text=i_sr)
		fig4.update_traces(texttemplate='%{y:.2s}',textposition='top center')
		st.plotly_chart(fig4)

	st.sidebar.markdown('### Final Scores')
	final_score=pd.DataFrame({'Team':team1,'score':final})
	#st.write(final_score)

	if st.sidebar.checkbox('Final Score',True,key=6):
		st.write('### This is the final score calculated out of 10,arranged in ascending order')
		fig5=px.funnel(final_score,x='score',y='Team',orientation='h')
		fig5.update_traces(texttemplate='%{x:.2s}')
		st.plotly_chart(fig5)


	#st.write(final)
	st.write('### The Team with Maximum Score is %s, with score %s '% (team1[7],final[7]))
	
if (password==("Rishabh BD") or password==("Sanjeev BD") or password==("Charles BD") or password==("Chandra BD") or password==("Soorabh BD") or password==("Dilip BD")):
	image_url='posterityfinal.png'
	image= Image.open(image_url) 
	st.image(image,width=350)
	
	st.title("BD Team PRS Dashboard")
	st.sidebar.title('Options ')
	st.markdown("### BD team's performance for the last month 📓" )
	st.write("This Dashboard has been prepared to give you a better insight into your BD Team's overall performance as well as give you an idea of where you stand in comparision to other team members")
	DATA_URL= 'BD Visuals.xlsx'
	

	#@st.cache(persist =True)
	def load_data():
		data=pd.read_excel(DATA_URL)

		return data 

	data = load_data()
	st.write(data)
	st.sidebar.subheader('Data Division')
	data['Companies Contacted']=data['Companies Contacted'].astype(int)
	data['E-Meetings Scheduled']=data['E-Meetings Scheduled'].astype(int)
	data['Meeting Targets']=data['Meeting Targets'].astype(int)
	data['Ongoing Projects']=data['Ongoing Projects'].astype(int)
	data['Failed Projects']=data['Failed Projects'].astype(int)
	data['Finished Projects']=data['Finished Projects'].astype(int)
	

	companies_contacted=data['Companies Contacted']
	meetings=data['E-Meetings Scheduled']
	ongoing_projects=data['Ongoing Projects']
	targets=data['Meeting Targets']
	op=data['Ongoing Projects']
	fp=data['Failed Projects']
	done=data['Finished Projects']
	
	names=data['Name'].to_list()
	
	st.write('Hover Over the Graphs to see the numbers')
	st.write(companies_contacted)
	if st.sidebar.checkbox('Show Number of Companies Contacted', True, key=1):
		fig=px.line(x=names,y=companies_contacted,text=companies_contacted)
		fig.update_traces(texttemplate='%{text:.2s}', textposition='top center')
		fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		st.plotly_chart(fig)
		
		
	st.write('### Meetings Scheduled')
	st.write('The graph shows, Target Vs Achieved for the meetings scheduled by the BD team.')
	fig1 = go.Figure(data=[
    	go.Bar(name='Target', x=names, y=targets),
    	go.Bar(name='Meetings Scheduled', x=names, y=meetings)
	])
	# Change the bar mode
	fig1.update_layout(barmode='group')
	st.plotly_chart(fig1)
	
	st.write('### Projects Mapping')
	st.write('This graphs represents the Ongoing Projects,Finished as well as Failed Projects')
		
	labels=['Ongoing Projects','Failed Projects','Finished Projects']
	fig10 = make_subplots(rows=1, cols=3, specs=[[{'type':'domain'}, {'type':'domain'},{'type':'domain'}]])
	fig10.add_trace(go.Pie(labels=labels, values=op, name="Rishabh"),1, 1)
	fig10.add_trace(go.Pie(labels=labels, values=fp, name="Sanjeev"),1, 2)
	fig10.add_trace(go.Pie(labels=labels, values=done, name="Charles"),1, 3)

	fig10.update_traces(hole=.4, hoverinfo="label+percent+name")
	fig10.update_layout(title_text="Projects Mapping",annotations=[dict(text='Rishabh', x=0.09, y=0.5, font_size=12, showarrow=False),
                dict(text='Sanjeev', x=0.50, y=0.5, font_size=12, showarrow=False),dict(text='Charles', x=0.90, y=0.5, font_size=12, showarrow=False)])
	st.plotly_chart(fig10)
	
		
		
	
	
	
	
