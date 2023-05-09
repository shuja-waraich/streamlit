
import openai
import streamlit as st
from streamlit_pills import pills
#import whisper
from st_custom_components import st_audiorec
import streamlit.components.v1 as components



openai.api_key = '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'

st.subheader("AI Assistant : Streamlit + OpenAI: `stream` ")

# You can also use radio buttons instead
selected = pills("", ["NO Streaming", "Streaming"], ["🎈", "🌈"])


def audiorec_demo_app():
    st.write('\n\n')


audio_file = st_audiorec()
audioflag=False


#user_input = st.text_input("You: ",placeholder = "Ask me anything ...", key="input")

if audio_file is not None:
    #model = whisper.load_model("medium")     
    #transcription = model.transcribe(audio_file.name)["text"]
    user_input = "hello"
    audioflag = True

    #audio_file is None or clear:
user_input = st.text_input("You: ",placeholder = "Ask me anything ...", key="input")



if st.button("Submit", type="primary") or audioflag:
    st.markdown("----")
    res_box = st.empty()
    print(user_input)
    completions = openai.Completion.create(model='text-davinci-003',
                                        prompt=user_input,
                                        max_tokens=120, 
                                        temperature = 0.5,
                                        stream = False)
    result = completions.choices[0].text
    print(user_input)
    res_box.write(result)
    
    
st.markdown("----")

audio_file = None