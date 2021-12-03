- area of software that understands written or spoken language

- QnA maker, Azure bot service
- https://aidemos.microsoft.com/luis/demo
- https://www.microsoft.com/en-us/research/project/health-bot/
- https://www.microsoft.com/en-us/research/project/health-bot/
- https://azure.microsoft.com/en-us/services/bot-services/health-bot/#overview

- https://docs.microsoft.com/en-us/learn/certifications/azure-ai-engineer/?tab=tab-learning-paths

Text analytics
--

- statistical analysis
- frequency analysis
- Stemming analysis: power/ powered
- Structure rules: Noun 
- numeric encoding
- vectorized models: flower/ plant kept together

- model returns: 
1) A score indicating a level of confidence in the language detection. 
confidence 0.8=The predominant language in the text is English.
confidence NaN=Text is ambiguous in nature

2) The language name
3) The ISO 6391 language code


key phrase extraction
--------
- summerize main points

Entity recognition
----

- item of particular type. Ex. Location, City, Artist
- https://docs.microsoft.com/en-us/learn/modules/analyze-text-with-text-analytics-service/3-exercise?launch-lab=true


Sentiment analysis
-----------
- sentiment score=0.5 => The texts do not have sufficient context to discern a sentiment
- score=0.65 => positive

Recognize and synthesize speech
----

** For an AI solution to accept vocal commands and provide spoken responses, what capabilities must the AI system support?
- Speech recognition
- Speech synthesis

- Speech recognition: read spoken voice
- https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support#speech-to-text
- uses Universal Language Model trained by MS: Conversational, Dictation
- real time transcription
- batch transcription
- Speech recognition uses Acoustic and language model
- Acoustic model: changes audio signal into phonemes
- Language model: maps phonemes to words

- Speech recognition -> Texts that can be spoken => Speech synthesis -> Spoken text

- Speech synthesis: voice menus, reading emails
- https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support#text-to-speech
- text to speech API

- https://docs.microsoft.com/en-us/learn/modules/recognize-synthesize-speech/3-exercise-transcribe-speech-use-azure?launch-lab=true



