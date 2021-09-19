# FALLABOUT-SRMMIC 21

# POETRY-GENERATION

## DESCRIPTION
 We have developed a NLP(natural language processing) model which automatically generates a poem
 based on the initial/promt text given as input by the user.
 
 # Motivation
  The majority of ML/DL models result is usualy based on the training/validation accuracy and loss.
  And one of the models which does not depend on either on accuracy or loss is NLP text generating model.
  Irrespective of the accuracy the generated text may or maynot make sense. Sometimes the accuracy can be very high
  and not give satisfactory results or end up in a loop. So this can only be done by looking at the result after many
  trails and training. 
  
 # Uses
  1. Can be used for creative and fun purposes.
  2. Can sometimes used for reproducing or generating the text for larger datasets.
  3. Literature purpose like understanding and analysing a certain poetric style.
  
 # What's unique?
  1. Unlike many poetry generation, we also built a hindi poetry text generation model.
  2. We provide an analysis for [LSTM](https://machinelearningmastery.com/stacked-long-short-term-memory-networks/#:~:text=A%20Stacked%20LSTM%20architecture%20can,for%20all%20input%20time%20steps.) layers and [transformers](https://www.analyticsvidhya.com/blog/2019/06/understanding-transformers-nlp-state-of-the-art-models/#:~:text=The%20Transformer%20in%20NLP%20is,long%2Drange%20dependencies%20with%20ease.&text=The%20idea%20behind%20Transformer%20is,with%20attention%20and%20recurrence%20completely.) with an example for better understanding.
 
 # Built with
  1. [Streamlit](https://streamlit.io/) for frontend
  2. _________ for hindi poetry (*Need to fill*)
  3. [aitextgen](https://docs.aitextgen.io/) for english poetry

 # Deeper into the project
  The english poetry generation is developed with the help of an open-sourse library known as *aitextgen*.
  The famous [GPT-2](https://openai.com/blog/better-language-models/) transformer is used in this project, finetuned on **Shakespeares** poems and sonnets alone.
  The front-end is simply handled by streamlit.
  **need some matter on hindi model**
  
 # Installation
  The `app.py` file should be installed and download the model from ~~this link~~. The trained_model folder
  should specify the path to your downloaded model. Finally `streamlit run app.py` in your terminal and enjoy
  the app.
  
  **need instructions for hindi**
  
 # Future works
  
