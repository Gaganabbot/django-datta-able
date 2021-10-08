from django.shortcuts import render
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import SkillsForm
import pandas as pd
import neattext.functions as nfx
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity,linear_kernel 

@login_required(login_url="/login/")
def SkillsLearning(request):
    val_rec=None
    value_df=None
    form = SkillsForm()
    if request.method == 'POST':
        print("entered post")
        
        form = SkillsForm(request.POST)
        if form.is_valid():
            print(form)
            item_Value = form['input_text'].value()
            val_rec=recommend_course(str(item_Value),10)
            df = pd.DataFrame(val_rec)
            if df is not None:
                value_df=df.to_numpy()
            form.save()

    context = {'segment': 'index','forms':form,'val_rec': value_df}
    html_template = loader.get_template('skills.html')
    return HttpResponse(html_template.render(context, request))

def recommend_course(title,num_of_rec=10):
    # ID for title
    import os
    course_list=os.getcwd()
    # print(course_list+"\\apps\\Skill\\udemy_courses.csv")
    df = pd.read_csv(course_list+"\\apps\\Skill\\udemy_courses.csv")
    dir(nfx)
    print(df)
    df['clean_subject']=df['subject'].apply(nfx.remove_stopwords)
    df['clean_subject']=df['clean_subject'].apply(nfx.remove_special_characters)
    print(df['clean_subject'])
    df['clean_course_title'] = df['course_title'].apply(nfx.remove_stopwords)
    df['clean_course_title'] = df['clean_course_title'].apply(nfx.remove_special_characters)
    df[['course_title','clean_course_title','clean_subject','subject']]
    count_vect = CountVectorizer()
    cv_mat = count_vect.fit_transform(df['clean_course_title'])
    cv_mat.todense()
    print(cv_mat)
    df_cv_words = pd.DataFrame(cv_mat.todense(),columns=count_vect.get_feature_names())
    cosine_sim_mat = cosine_similarity(cv_mat)
    course_indices = pd.Series(df.index,index=df['course_title']).drop_duplicates()
    idx = course_indices[title]
    scores = list(enumerate(cosine_sim_mat[idx]))
    sorted_scores = sorted(scores,key=lambda x:x[1],reverse=True)
    selected_course_indices = [i[0] for i in sorted_scores[1:]]
    selected_course_scores = [i[1] for i in sorted_scores[1:]]

    result = df['course_title'].iloc[selected_course_indices]
    result_sub= df['subject'].iloc[selected_course_indices]
    result_url = df['url'].iloc[selected_course_indices]
    result_review = df['content_duration'].iloc[selected_course_indices]
    
    rec_df = pd.DataFrame(result)
    rec_df['subject']=result_sub
    rec_df['url']=result_url
    rec_df['content_duration']=result_review
    rec_df['similarity_scores'] = selected_course_scores
    return rec_df.head(num_of_rec)