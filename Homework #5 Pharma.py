
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


import matplotlib as mpl


# In[4]:


import matplotlib.pyplot as plt


# In[5]:


import seaborn as seb


# In[6]:


file1 = "D:/clinicaltrial_data.csv"


# In[7]:


file2 = "D:/mouse_drug_data.csv"


# In[77]:


clinical_trial_df = pd.read_csv(file1, low_memory=False)


# In[78]:


mouse_drug_df = pd.read_csv(file2, low_memory=False)


# In[79]:


clinical_trial_df.head()


# In[80]:


mouse_drug_df.head()


# In[81]:


clinical_trial_df.isnull().sum()


# In[83]:


mouse_drug_df.isnull().sum()


# In[82]:


clinical_trial_df.dtypes


# In[84]:


mouse_drug_df.dtypes


# In[85]:


combined_data = pd.merge(clinical_trial_df,mouse_drug_df, on="Mouse ID")
combined_data = combined_data.rename(columns={"Tumor Volume (mm3)":"Tumor Volume in cubic millimeters"})
combined_data.head()


# In[86]:


combined_data.columns


# In[18]:


mouse_check = combined_data['Mouse ID'].drop_duplicates()
mouse_check.value_counts();


# In[19]:


combined_data['Timepoint'].value_counts()


# In[20]:


combined_data['Drug'].value_counts()


# In[21]:


Capomulin_df = combined_data.loc[combined_data['Drug'] == 'Capomulin']
Capomulin_df.head()


# In[22]:


Capomulin_df.dtypes


# In[23]:


Capo_x_axis = Capomulin_df['Timepoint']
Capo_x_axis;


# In[24]:


Capo_y_axis = Capomulin_df['Tumor Volume in cubic millimeters']


# In[25]:


plt.title("Capomulin Time Frame & Tumor Volume Data")
plt.xlabel("Timepoint")
plt.ylabel("Tumor Volume mm^3")
plt.scatter(Capo_x_axis, Capo_y_axis, marker = 'o', facecolors = "red", edgecolors="black")
seb.set()
seb.set_style("whitegrid")


# In[26]:


Capo_tumor_mean = Capomulin_df.groupby('Timepoint', as_index=False)['Tumor Volume in cubic millimeters'].mean()
Capo_tumor_mean


# In[27]:


Capo_tumor_sem = Capomulin_df.groupby('Timepoint', as_index=False)['Tumor Volume in cubic millimeters'].sem()
Capo_tumor_sem = Capo_tumor_sem.fillna(0)
Capo_tumor_sem


# In[28]:


plt.errorbar(np.arange(0,50,5), Capo_tumor_mean['Tumor Volume in cubic millimeters'], yerr=Capo_tumor_sem['Tumor Volume in cubic millimeters'], color="b",alpha=0.5)

plt.title("Mean and Standard Error of Tumor Volume for Testing Capomulin")
plt.xlabel("Timepoint")
plt.ylabel("Tumor Volume mm^3")

plt.legend(loc="upper right", fontsize="small", fancybox=True)
seb.set()
seb.set_style("whitegrid")
plt.show()


# In[29]:


Capo_x_axis = Capomulin_df['Timepoint']
Capo_y_axis = Capomulin_df['Metastatic Sites']
plt.title("Capomulin Time Frame & Metastatic Site Data")
plt.xlabel("Timepoint")
plt.ylabel("Metastatic Sites")
plt.scatter(Capo_x_axis, Capo_y_axis, marker = 'o', facecolors = "red", edgecolors="black")
seb.set()
seb.set_style("whitegrid")


# In[30]:


Capo_Metastatic_mean = Capomulin_df.groupby('Timepoint', as_index=False)['Metastatic Sites'].mean()
Capo_Metastatic_mean


# In[31]:


Capo_Metastatic_sem = Capomulin_df.groupby('Timepoint', as_index=False)['Metastatic Sites'].sem()
Capo_Metastatic_sem = Capo_Metastatic_sem.fillna(0)
Capo_Metastatic_sem


# In[32]:


plt.errorbar(np.arange(0,50,5), Capo_Metastatic_mean['Metastatic Sites'], yerr=Capo_Metastatic_sem['Metastatic Sites'], color="b",alpha=0.5)


plt.title("Mean and Standard Error of Metastatic Sites for Testing Capomulin")
plt.xlabel("Timepoint")
plt.ylabel("Metastatic Sites")



plt.legend(loc="upper left", fontsize="small", fancybox=True)

seb.set()
seb.set_style("whitegrid")

plt.show()


# In[33]:


Capo_time_calc = Capomulin_df['Timepoint'].value_counts()
Capo_time_calc = Capo_time_calc.to_frame()
Capo_time_calc['Time Value'] = Capo_time_calc.index
Capo_time_calc = Capo_time_calc.rename(columns={"Timepoint":"Number of Mice"})
Capo_time_calc.sort_index()


# In[34]:


Capo_x_axis = Capo_time_calc['Time Value']
Capo_y_axis = Capo_time_calc['Number of Mice']
plt.title("Survivability Rate of Mice During Drug Testing")
plt.xlabel("Timepoint")
plt.ylabel("Number of Mice Alive During Testing")
plt.scatter(Capo_x_axis, Capo_y_axis, marker = 'o', facecolors = "red", edgecolors="black")
seb.set()
seb.set_style("whitegrid")


# In[35]:


Capo_Metastatic_mean = Capomulin_df.groupby('Timepoint', as_index=False)['Metastatic Sites'].mean()
Capo_Metastatic_mean


# In[36]:


Ketapril_df = combined_data.loc[combined_data['Drug'] == 'Ketapril']
Ketapril_df.head()


# In[37]:


plt.title("Ketapril Time Frame & Tumor Volume Data")
Keta_x_axis = Ketapril_df['Timepoint']
Keta_y_axis = Ketapril_df['Tumor Volume in cubic millimeters']
plt.xlabel("Timepoint")
plt.ylabel("Tumor Volume mm^3")
plt.scatter(Keta_x_axis, Keta_y_axis, marker = 'o', facecolors = "red", edgecolors="black")
seb.set()
seb.set_style("whitegrid")


# In[38]:


Keta_tumor_mean = Ketapril_df.groupby('Timepoint', as_index=False)['Tumor Volume in cubic millimeters'].mean()
Keta_tumor_mean


# In[39]:


Keta_tumor_sem = Ketapril_df.groupby('Timepoint', as_index=False)['Tumor Volume in cubic millimeters'].sem()
Keta_tumor_sem = Keta_tumor_sem.fillna(0)
Keta_tumor_sem


# In[40]:


plt.errorbar(np.arange(0,50,5), Keta_tumor_mean['Tumor Volume in cubic millimeters'], yerr=Keta_tumor_sem['Tumor Volume in cubic millimeters'], color="b",alpha=0.5)

plt.title("Mean and Standard Error of Tumor Volume for Testing Ketapril")
plt.xlabel("Timepoint")
plt.ylabel("Tumor Volume in mm^3")

plt.legend(loc="upper left", fontsize="small", fancybox=True)
seb.set()
seb.set_style("whitegrid")

plt.show()


# In[41]:


Keta_x_axis = Ketapril_df['Timepoint']
Keta_y_axis = Ketapril_df['Metastatic Sites']
plt.title("Ketapril Time Frame & Metastatic Site Data")
plt.xlabel("Timepoint")
plt.ylabel("Metastatic Sites")
plt.scatter(Keta_x_axis, Keta_y_axis, marker = 'o', facecolors = "red", edgecolors="black")
seb.set()
seb.set_style("whitegrid")


# In[42]:


Keta_Metastatic_mean = Ketapril_df.groupby('Timepoint', as_index=False)['Metastatic Sites'].mean()
Keta_Metastatic_mean


# In[43]:


Keta_Metastatic_sem = Ketapril_df.groupby('Timepoint', as_index=False)['Metastatic Sites'].sem()
Keta_Metastatic_sem = Keta_Metastatic_sem.fillna(0)
Keta_Metastatic_sem


# In[44]:


plt.errorbar(np.arange(0,50,5), Keta_Metastatic_mean['Metastatic Sites'], yerr=Keta_Metastatic_sem['Metastatic Sites'], color="b",alpha=0.5)

plt.title("Mean and Standard Error of Metastatic Sites for Testing Ketapril")
plt.xlabel("Timepoint")
plt.ylabel("Metastatic Sites")

plt.legend(loc="upper left", fontsize="small", fancybox=True)

seb.set()
seb.set_style("whitegrid")

plt.show()


# In[45]:


Keta_time_calc = Ketapril_df['Timepoint'].value_counts()
Keta_time_calc = Keta_time_calc.to_frame()
Keta_time_calc['Time Value'] = Keta_time_calc.index
Keta_time_calc = Keta_time_calc.rename(columns={"Timepoint":"Number of Mice"})
Keta_time_calc.sort_index()


# In[46]:


Keta_x_axis = Keta_time_calc['Time Value']
Keta_y_axis = Keta_time_calc['Number of Mice']
plt.title("Survivability Rate of Mice During Drug Testing")
plt.xlabel("Timepoint")
plt.ylabel("Number of Mice Alive During Testing")
plt.scatter(Keta_x_axis, Keta_y_axis, marker = 'o', facecolors = "red", edgecolors="black")
seb.set()
seb.set_style("whitegrid")


# In[47]:


Placebo_df = combined_data.loc[combined_data['Drug'] == 'Placebo']
Placebo_df.head();


# In[48]:


plt.title("Placebo Time Frame & Tumor Volume Data")
Plac_x_axis = Placebo_df['Timepoint']
Plac_y_axis = Placebo_df['Tumor Volume in cubic millimeters']
plt.xlabel("Timepoint")
plt.ylabel("Tumor Volume mm^3")
plt.scatter(Plac_x_axis, Plac_y_axis, marker = 'o', facecolors = "red", edgecolors="black")
seb.set()
seb.set_style("whitegrid")


# In[49]:


Plac_tumor_mean = Placebo_df.groupby('Timepoint', as_index=False)['Tumor Volume in cubic millimeters'].mean()
Plac_tumor_mean


# In[50]:


Plac_tumor_sem = Placebo_df.groupby('Timepoint', as_index=False)['Tumor Volume in cubic millimeters'].sem()
Plac_tumor_sem = Plac_tumor_sem.fillna(0)
Plac_tumor_sem


# In[51]:


plt.errorbar(np.arange(0,50,5), Plac_tumor_mean['Tumor Volume in cubic millimeters'], yerr=Plac_tumor_sem['Tumor Volume in cubic millimeters'], color="b",alpha=0.5)

plt.title("Mean and Standard Error of Tumor Volume for Testing Placebo")
plt.xlabel("Timepoint")
plt.ylabel("Tumor Volume in mm^3")

plt.legend(loc="upper left", fontsize="small", fancybox=True)

seb.set()
seb.set_style("whitegrid")

plt.show()


# In[52]:


plt.title("Placebo Time Frame & Metastatic Site Data")
Plac_x_axis = Placebo_df['Timepoint']
Plac_y_axis = Placebo_df['Metastatic Sites']
plt.xlabel("Timepoint")
plt.ylabel("Tumor Volume mm^3")
plt.scatter(Plac_x_axis, Plac_y_axis, marker = 'o', facecolors = "red", edgecolors="black")
seb.set()
seb.set_style("whitegrid")


# In[53]:


Plac_Metastatic_mean = Placebo_df.groupby('Timepoint', as_index=False)['Metastatic Sites'].mean()
Plac_Metastatic_mean


# In[54]:


Plac_Metastatic_sem = Placebo_df.groupby('Timepoint', as_index=False)['Metastatic Sites'].sem()
Plac_Metastatic_sem = Plac_Metastatic_sem.fillna(0)
Plac_Metastatic_sem


# In[55]:


plt.errorbar(np.arange(0,50,5), Plac_Metastatic_mean['Metastatic Sites'], yerr=Plac_Metastatic_sem['Metastatic Sites'], color="b",alpha=0.5)

plt.title("Mean and Standard Error of Metastatic Sites for Testing Placebo")
plt.xlabel("Timepoint")
plt.ylabel("Metastatic Sites")

plt.legend(loc="upper left", fontsize="small", fancybox=True)

seb.set()
seb.set_style("whitegrid")

plt.show()


# In[56]:


Plac_time_calc = Placebo_df['Timepoint'].value_counts()
Plac_time_calc = Plac_time_calc.to_frame()
Plac_time_calc['Time Value'] = Plac_time_calc.index
Plac_time_calc = Plac_time_calc.rename(columns={"Timepoint":"Number of Mice"})
Plac_time_calc.sort_index()


# In[57]:


Plac_x_axis = Plac_time_calc['Time Value']
Plac_y_axis = Plac_time_calc['Number of Mice']
plt.title("Survivability Rate of Mice During Drug Testing")
plt.xlabel("Timepoint")
plt.ylabel("Number of Mice Alive During Testing")
plt.scatter(Plac_x_axis, Plac_y_axis, marker = 'o', facecolors = "red", edgecolors="black")
seb.set()
seb.set_style("whitegrid")


# In[58]:


Infubinol_df = combined_data.loc[combined_data['Drug'] == 'Infubinol']
Infubinol_df.head()


# In[59]:


plt.title("Infubinol Time Frame & Tumor Volume Data")
Infub_x_axis = Infubinol_df['Timepoint']
Infub_y_axis = Infubinol_df['Tumor Volume in cubic millimeters']
plt.xlabel("Timepoint")
plt.ylabel("Tumor Volume mm^3")
plt.scatter(Infub_x_axis, Infub_y_axis, marker = 'o', facecolors = "red", edgecolors="black")
seb.set()
seb.set_style("whitegrid")


# In[60]:


Infub_tumor_mean = Infubinol_df.groupby('Timepoint', as_index=False)['Tumor Volume in cubic millimeters'].mean()
Infub_tumor_mean


# In[61]:


Infub_tumor_sem = Infubinol_df.groupby('Timepoint', as_index=False)['Tumor Volume in cubic millimeters'].sem()
Infub_tumor_sem = Infub_tumor_sem.fillna(0)
Infub_tumor_sem


# In[62]:


plt.errorbar(np.arange(0,50,5), Infub_tumor_mean['Tumor Volume in cubic millimeters'], yerr=Infub_tumor_sem['Tumor Volume in cubic millimeters'], color="b",alpha=0.5)

plt.title("Mean and Standard Error of Tumor Volume for Testing Infubinol")
plt.xlabel("Timepoint")
plt.ylabel("Tumor Volume in mm^3")

plt.legend(loc="upper left", fontsize="small", fancybox=True)

seb.set()
seb.set_style("whitegrid")

plt.show()


# In[63]:


plt.title("Infubinol Time Frame & Metastatic Site Data")
Infub_x_axis = Infubinol_df['Timepoint']
Infub_y_axis = Infubinol_df['Metastatic Sites']
plt.xlabel("Timepoint")
plt.ylabel("Tumor Volume mm^3")
plt.scatter(Infub_x_axis, Infub_y_axis, marker = 'o', facecolors = "red", edgecolors="black")

seb.set()
seb.set_style("whitegrid")


# In[64]:


Infub_Metastatic_mean = Infubinol_df.groupby('Timepoint', as_index=False)['Metastatic Sites'].mean()
Infub_Metastatic_mean


# In[65]:


Infub_Metastatic_sem = Infubinol_df.groupby('Timepoint', as_index=False)['Metastatic Sites'].sem()
Infub_Metastatic_sem = Infub_Metastatic_sem.fillna(0)
Infub_Metastatic_sem


# In[66]:


plt.errorbar(np.arange(0,50,5), Infub_Metastatic_mean['Metastatic Sites'], yerr=Infub_Metastatic_sem['Metastatic Sites'], color="b",alpha=0.5)

plt.title("Mean and Standard Error of Metastatic Sites for Testing Infubinol")
plt.xlabel("Timepoint")
plt.ylabel("Metastatic Sites")

plt.legend(loc="upper left", fontsize="small", fancybox=True)

seb.set()
seb.set_style("whitegrid")

plt.show()


# In[67]:


Infub_time_calc = Infubinol_df['Timepoint'].value_counts()
Infub_time_calc = Infub_time_calc.to_frame()
Infub_time_calc['Time Value'] = Infub_time_calc.index
Infub_time_calc = Infub_time_calc.rename(columns={"Timepoint":"Number of Mice"})
Infub_time_calc.sort_index()


# In[68]:


Infub_x_axis = Infub_time_calc['Time Value']
Infub_y_axis = Infub_time_calc['Number of Mice']
plt.title("Survivability Rate of Mice During Drug Testing")
plt.xlabel("Timepoint")
plt.ylabel("Number of Mice Alive During Testing")
plt.scatter(Infub_x_axis, Infub_y_axis, marker = 'o', facecolors = "red", edgecolors="black")
seb.set()
seb.set_style("whitegrid")


# In[69]:


Capo_tumor_gain_day45 = Capo_tumor_mean.loc[Capo_tumor_mean['Timepoint'] == 45, 'Tumor Volume in cubic millimeters']
Capo_tumor_gain_day0 = Capo_tumor_mean.loc[Capo_tumor_mean['Timepoint'] == 0, 'Tumor Volume in cubic millimeters']
Percent_Tumor_Volume_Change_Capo =((float(Capo_tumor_gain_day45)-Capo_tumor_gain_day0)/Capo_tumor_gain_day0)*100
Percent_Tumor_Volume_Change_Capo


# In[70]:


Keta_tumor_gain_day45 = Keta_tumor_mean.loc[Keta_tumor_mean['Timepoint'] == 45, 'Tumor Volume in cubic millimeters']
Keta_tumor_gain_day0 = Keta_tumor_mean.loc[Keta_tumor_mean['Timepoint'] == 0, 'Tumor Volume in cubic millimeters']
Percent_Tumor_Volume_Change_Keta =((float(Keta_tumor_gain_day45)-Keta_tumor_gain_day0)/Keta_tumor_gain_day0)*100
Percent_Tumor_Volume_Change_Keta


# In[71]:


Plac_tumor_gain_day45 = Plac_tumor_mean.loc[Plac_tumor_mean['Timepoint'] == 45, 'Tumor Volume in cubic millimeters']
Plac_tumor_gain_day0 = Plac_tumor_mean.loc[Plac_tumor_mean['Timepoint'] == 0, 'Tumor Volume in cubic millimeters']
Percent_Tumor_Volume_Change_Plac =((float(Plac_tumor_gain_day45)-Plac_tumor_gain_day0)/Plac_tumor_gain_day0)*100
Percent_Tumor_Volume_Change_Plac


# In[72]:


Infub_tumor_gain_day45 = Infub_tumor_mean.loc[Infub_tumor_mean['Timepoint'] == 45, 'Tumor Volume in cubic millimeters']
Infub_tumor_gain_day0 = Infub_tumor_mean.loc[Infub_tumor_mean['Timepoint'] == 0, 'Tumor Volume in cubic millimeters']
Percent_Tumor_Volume_Change_Infub =((float(Infub_tumor_gain_day45)-Infub_tumor_gain_day0)/Infub_tumor_gain_day0)*100
Percent_Tumor_Volume_Change_Infub


# In[75]:


Drugs = [Percent_Tumor_Volume_Change_Capo[0],Percent_Tumor_Volume_Change_Keta[0],Percent_Tumor_Volume_Change_Plac[0],Percent_Tumor_Volume_Change_Infub[0]]
x_axis = np.arange(0,len(Drugs),1)
bar_list = plt.bar(x_axis, Drugs, color='r', alpha=0.5, align="center")
bar_list[0].set_color('g')
bar_list
plt.title("Percent Tumor Growth During 45 Day Testing Process")
tick_locations = [value for value in x_axis]
plt.xticks(tick_locations, ["Capomulin", "Ketapril", "Placebo", "Infubinol"])
plt.ylabel("Percent")
plt.hlines(0, -.5, 3.5, alpha=0.25)
seb.set()
seb.set_style("whitegrid")

