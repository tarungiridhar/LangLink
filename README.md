# LangLink, Winner of HooHacks 2023 category "Most Creative Use of Twilio"

## Devpost:
https://devpost.com/software/midigo

LangLink is a peer-to-peer messaging service that is built using Twilio's bot messaging API. By simply registering your name and preferred language, you can communicate with anyone across the world with any language. By harnessing the power of Microsoft Azure's neural network translation API, we have built an application that breaks down barriers and increases accessibility as it allows people to easily communicate without having to be fluent in the same language.

## Inspiration
We were inspired to break down the language barriers that we had seen occurring in our day-to-day lives. As we know many people who live in the US who are not fluent in English, we wanted to create an application that can help increase the accessibility of not only those we care about, but also many around the world.

## What It Does
LangLink is a peer-to-peer messaging service. By connecting to another person to message, LangLink uses Microsoft Azure's powerful translation models to automatically translate any message into the language that you're most familiar with. This means that regardless of what language you can speak or read, you can communicate with someone easily using our app. 

## How We Built It
We laid out a pipeline that would allow us to take advantage of Twilio's programmable SMS. Since the programmable SMS is primarily intended for users to interact with a chatbot, we set up a conceptual method on how we can use it to send and process messages that are supposed to get sent to other people. As a result, we were able to cleanly translate the pipeline into Python code split up into a frontend and a backend. So when a user connects to another user, a user sends a message to Twilio, which then sends the message into Microsoft Azure's neural network translation model. This translated message is sent back to Twilio, which sends the translated message to the intended user.

## Challenges We Ran Into
The main challenge we ran into involved taking the bot-to-person communication style of Twilio, and translating that into the peer-to-peer messaging system that we needed. We spent hours conceptually planning out how to keep track of message history and how to make sure a message is properly sent to the recipient. 

## Accomplishments That We're Proud Of
It works. For our first hackathon, we are very elated to produce a finished product that has the same layout that we planned it to. The sheer fact that we were able to come together to put together something meaningful for us is what we believe is a huge accomplishment. Originally, we had spent long hours planning out and researching a completely different project, when last minute we were unable to put it all together the way we wanted. We switched gears once we had that realization, and took the individual parts of that project to put together LangLink as it is now. As a result, we are proud of our work done today and hope you too can see the passion that we have put into it.
