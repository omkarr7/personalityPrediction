import numpy as np
import matplotlib.pyplot as plt
import streamlit as st 
from util import get_info
import matplotlib.ticker as tk
import seaborn as sns
import json
import requests
from streamlit_lottie import st_lottie
value_inp = False 

st.set_page_config(layout='wide')

def gradientbars(bars):
    grad = np.atleast_2d(np.linspace(0,1,256)).T # Gradient of your choice

    rectangles = bars.containers[0]
    # ax = bars[0].axes
    fig, ax = plt.subplots()

    xList = []
    yList = []
    for rectangle in rectangles:
        x0 = rectangle._x0
        x1 = rectangle._x1
        y0 = rectangle._y0
        y1 = rectangle._y1

        xList.extend([x0,x1])
        yList.extend([y0,y1])

        ax.imshow(grad, extent=[x0,x1,y0,y1], aspect="auto", zorder=0)

    ax.axis([min(xList), max(xList), min(yList), max(yList)*1.1]) # *1.1 to add some buffer to top of plot

    return fig,ax

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_lottie_file(filepath: str):
    with open(filepath,'r') as f:
        return json.load(f)

# mood_url = 'https://assets3.lottiefiles.com/private_files/lf30_XVyB0O.json'
mood_url = 'mood.json'
# mood = load_lottieurl(mood_url)
mood = load_lottie_file(mood_url)

# _left , _right = st.columns([2,1])
# with _right:
#     st_lottie(mood,key='mood',height=350,width=550)
# with _left:
st.title('Personality Prediction')

col2,col3 = st.columns([3,1])
with col2:
    a = st.text_input('Enter email id (used while filling the google form)')

user_input = a
try:
    my_sums = get_info(user_input)
    columns=['open','conscientious','extraversion','agreeable','neurotic']
    my_sum = my_sums[['open','conscientious','extroversion','agreeable','neurotic','cluster']]
    my_sum = my_sum.drop('cluster',axis='columns')
    my_sum.columns = ['Neurotism','Agreeableness','Extraversion','Conscientness','Openness']
    my_sum.columns = ['Openness','Conscientiousness','Extraversion','Agreeableness','Neuroticsm']
except:
    pass

col1,col4,col5 = st.columns([1,3,1])
with col4:
    try:
        fig = plt.figure(1, (8,6))
        sns.set(style="whitegrid", color_codes=True)
        ax = fig.add_subplot(1,1,1)
        fmt = '%.0f%%' # Format you want the ticks, e.g. '40%'
        xticks = tk.FormatStrFormatter(fmt)
        ax.xaxis.set_major_formatter(xticks)
        seabornAxHandle = sns.barplot(y=my_sum.columns, x=my_sum.loc[0,:], palette="Greens_d")
        plt.xlim(0,100)
        st.write(fig)
    except:
        pass


st.markdown('''<h2 style="display:inline-block;color:purple">RESULTS</h2>''',True)

# result for openness
try:
    if my_sums['open'][0] > 65:
        st.markdown(
            '''
            With regard to <span style="color: orange;
                font-size: 40px;
                display: inline-block;
                font-weight: 600;">O</span>penness, you have a general appreciation for art, 
            emotion, adventure, unusual ideas and a variety of experiences.are willing to
            take new experiences in their stride. You cope well with with changes at work but will struggle with 
            repetitive, mundane tasks that lack creativity and require logic. 
        ''',True
        )
    elif 35< my_sums['open'][0] < 65:
        st.markdown(
            '''
            With regard to <span style="color: orange;
                font-size: 40px;
                display: inline-block;
                font-weight: 600;">O</span>penness, You have a medium level of openness 
                to experience. At times, you can be very creative, curious, and adventurous. 
                At other times, you prefer routine. You are able to find a great balance between
                ideas and practicality.
        ''',True
        )
    else:
        st.markdown(
            ''' 
            <style>
            span{
                color: orange;
                font-size: 40px;
                display: inline-block;
                font-weight: 600;
            }
            </style>
            With regard to <span>O</span>penness, you typically prefer methodical 
            and logical approaches to their work. You are less likely to embrace change,
            preferring to maintain the status quo in terms of their work style. 
            ''',True
        )
except:
    pass

# result for conscientiousnes
try:
    if my_sums['conscientious'][0] > 50:
        st.markdown(
            '''
            With regard to <span style="color: orange;
                font-size: 40px;
                display: inline-block;
                font-weight: 600;">C</span>onscientiousness, you generally prefer structured,
                 ordered approaches to their work. They are not only ambitious but will also use
                  their determination and preparedness to achieve their goals
        ''',True
        )
    elif 35< my_sums['conscientious'][0] < 65:
        st.markdown(
            '''
            With regard to <span style="color: orange;
                font-size: 40px;
                display: inline-block;
                font-weight: 600;">C</span>onscientiousness, You scored medium on conscientiousness. 
                At times, you are very driven and hard-working, but that doesnt mean you dont
                like to have fun! You are always able to set a comfortable balance between work and fun.
        ''',True
        )
    else:
        st.markdown(
            ''' 
            <style>
            span{
                color: orange;
                font-size: 40px;
                display: inline-block;
                font-weight: 600;
            }
            </style>
            With regard to <span>C</span>onscientiousness, You are typically laid-back and relaxed,
            and tend not to get too worked up about things. You truly like to enjoy life.  
            You can be a procrastinator, and you sometimes tend to put off your responsibilities until the
            last minute. If something fun comes up, it doesnt bother you to put your responsibilities off until the next day.
            ''',True
        )
except:
    pass
# result for extraversion
try:
    if my_sums['extroversion'][0] > 50:
        st.markdown(
            '''
            With regard to <span style="color: orange;
                font-size: 40px;
                display: inline-block;
                font-weight: 600;">E</span>xtraversion, you are typically energized when interacting 
                with co-workers, and tend to be more productive in team discussions. However, working
                independently might <strong>sometimes</strong> be a challenge for you due a high extraversion score.
        ''',True
        )
    elif 35< my_sums['extroversion'][0] < 65:
        st.markdown(
            '''
            With regard to <span style="color: orange;
                font-size: 40px;
                display: inline-block;
                font-weight: 600;">E</span>xtraversion, you get your energy from being around 
                others; but at other times, you get your energy by being alone. Life is all about balance, 
                and for you, its important to spend time alone and with others. You dont mind being the 
                center of attention at times, but you dont seek out ways to be the center of attention 
                either.
        ''',True
        )
    else:
        st.markdown(
            ''' 
            <style>
            span{
                color: orange;
                font-size: 40px;
                display: inline-block;
                font-weight: 600;
            }
            </style>
            With regard to <span>E</span>xtraversion, youmight prefer working independently on 
            projects and achieve their best work working alone. You might tend to struggle with 
            collaborating or discussing ideas with team members. 
            ''',True
        )
except:
    pass
# result for agreeableness
try:
    if my_sums['agreeable'][0] > 50:
        st.markdown(
            '''
            With regard to <span style="color: orange;
                font-size: 40px;
                display: inline-block;
                font-weight: 600;">A</span>greeableness, you are likely to assist others with 
                challenging tasks. You are also happy to collaborate with team members and work 
                towards resolving problems in the workplace. In other words, their agreeable trait 
                makes them good problem solvers
        ''',True
        )
    elif 35< my_sums['agreeable'][0] < 65:
        st.markdown(
            '''
            With regard to <span style="color: orange;
                font-size: 40px;
                display: inline-block;
                font-weight: 600;">A</span>greeableness, Others often describe you as friendly 
                and helpful. You typically try to avoid conflict, but when a situation arises, you 
                arent afraid to speak up. In group situations, you are able to find a comfortable 
                balance between keeping everyone happy, but also speaking up and making the right 
                decision.
        ''',True
        )
    else:
        st.markdown(
            ''' 
            <style>
            span{
                color: orange;
                font-size: 40px;
                display: inline-block;
                font-weight: 600;
            }
            </style>
            With regard to <span>A</span>greeableness, you might tend to be more forceful with 
            their opinions. You can be headstrong in their ideas. This means you might need to work 
            on being more sympathetic to others' views 
            and try to ensure they listen to other team members perspectives more.
            ''',True
        )
except:
    pass
# result for neurotic
try:
    if my_sums['neurotic'][0] > 50:
        st.markdown(
            '''
            With regard to <span style="color: orange;
                font-size: 40px;
                display: inline-block;
                font-weight: 600;">N</span>euroticism, you may typically find working in high-pressure
                situations a challenge. You prefer calmer work environments, which make it easier for you
                 to avoid stress. In high-pressure work situations, you are likely to struggle with 
                 your emotions and be highly concerned when you 
                 make mistakes.
        ''',True
        )
    elif 35< my_sums['neurotic'][0] < 65:
        st.markdown(
            '''
            With regard to <span style="color: orange;
                font-size: 40px;
                display: inline-block;
                font-weight: 600;">N</span>euroticism, You are moderately neurotic at times,
                 you can be anxious or emotional, while at other times, you are relaxed and calm.
                  Your mood may fluctuate slightly, depending on the day.
        ''',True
        )
    else:
        st.markdown(
            ''' 
            <style>
            span{
                color: orange;
                font-size: 40px;
                display: inline-block;
                font-weight: 600;
            }
            </style>
            With regard to <span>N</span>euroticism, you an work in a more stable, predictable way, 
            despite high-pressure situations. You will also have a more positive outlook 
            in terms of challenging projects and are generally more optimistic. Staying calm where others
            might become stressed in the workplace comes naturally to those who have a low neuroticism 
            score.
            ''',True
        )
except:
    pass