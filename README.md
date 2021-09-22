# FALLABOUT-SRMMIC 21

# POETRY-GENERATION
## HINGLISH

# DESCRIPTION
 We have developed a [NLP](https://www.ibm.com/cloud/learn/natural-language-processing#:~:text=Natural%20language%20processing%20(NLP)%20refers,same%20way%20human%20beings%20can.)(natural language processing) model which automatically generates a poem
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
  2. [tensorflow keras](https://www.tensorflow.org/api_docs/python/tf/keras) for hindi poetry
  3. [aitextgen](https://docs.aitextgen.io/) for english poetry

 # Deeper into the project
  The english poetry generation is developed with the help of an open-sourse library known as *aitextgen*.
  The famous [GPT-2](https://openai.com/blog/better-language-models/) transformer is used in this project, finetuned on **Shakespeares** poems and sonnets alone.
  The hindi poetry generation is built with tensorflow keras. 
  The front-end is simply handled by streamlit.
  
  [Here](https://colab.research.google.com/drive/1xhwGXiygKPy-C8Hh2Pf4BB4X81BlKL9f) is an example of how aitextgen is fine tuned.
  [Here](https://colab.research.google.com/drive/1-FhswLVmySN73gHGKzBKI0sXBw0tXh3_) is an example on how to train your own model using tensorflow keras.
  
 # A peek into our project
 
  ![hindiNLP](https://user-images.githubusercontent.com/79344352/134283716-672890d4-33bb-470e-a413-cfd3bb534b3d.PNG)
  
  ![EnglishNLP](https://user-images.githubusercontent.com/79344352/134283837-23ed5f0c-f2f3-4000-be23-2673e91d9b9b.PNG)
  
 # Installation
  The `app.py` file should be installed and download the model from [this link](https://drive.google.com/drive/folders/1kbYcl0piU_2O5SG7ndIFGDYH4TDuLd1c?usp=sharing). The trained_model folder
  should specify the path to your downloaded model. And you have to install trained_model_hindi from [this link](https://drive.google.com/drive/folders/17NzDdcCaHBwQCWbSmsUDpv-VLU_dzwZX?usp=sharing) and specify the path as above.
  The trained_model_hindi forlder contains the trained model, tokenizer and etc. Similarly the trained_model folder for english also contains the model 
  and uses the default built in GPT-2 transformer.
  Finally `streamlit run app.py` in your terminal and enjoy
  the app.
 
  ![FALLABOUT SRM](https://user-images.githubusercontent.com/79344352/134283027-1cb8a8c1-f6b9-4f86-85ca-5ce9b9fef05e.PNG)
   
   This is how Your code should look while running on local.
 
 # Future works
  1. Planning on including a translator to slide easily between languages.
  2. Introduce more poet based model in many languages.  

# Authors
 1. Paras Rawat
 2. Daketi Yatin
