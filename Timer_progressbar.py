import streamlit as st
import time as ts
from datetime import time
st.title("Uploading Files")
images=st.file_uploader("Please upload an image", type=["jpg","png"],accept_multiple_files=True)
if images is not None:
    for image in images:
     st.image(image)
    
# for vedio
#image=st.file_uploader("Please upload an image", type"mp4")
#if image is not None:
#    st.vedio(image)

m=st.slider("This is a slider",min_value=50, max_value=100,value=70)
print(m)
val2=st.text_input("Enter your Course Tittle",max_chars=60)
print(val2)
value=st.text_area("Course Description",max_chars=60)
print(value)

# Timer with Progress bar
def converter(value):
    m,s,ms=value.split(":")
    t_s=int(m)*60+int(s)+int(ms)/1000
    return t_s
val=st.time_input("Set Timer",value=time(0,0,0))


if str(val)=="00:00:00":
    st.write("Please set Timer")
else:
    sec=converter(str(val))
    print(sec)
    bar=st.progress(0)
    per=sec/100
    progress_status=st.empty()
    for i in range(100):
     bar.progress(i+1)
     progress_status.write(str(i+1) + " % ")
     ts.sleep(per)