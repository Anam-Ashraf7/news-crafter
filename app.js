
// const childProcess = require('child_process');
const language =document.getElementById("languages")
const date=document.getElementById("date")

let arr = []
function next() {
  const category=document.getElementById("input")
  const date = document.getElementById("date")
const container=document.getElementById("container")
let arr = [] 
  console.log(date.value)
  
  fetch(`https://gnews.io/api/v4/search?q=${category.value}&from=${date.value}T00:00:00Z&to=${date.value}T23:59:59Z&apikey=08a5e1a36c67321d59b30556f54ca166&lang=en`)
  .then(res => res.json())
  .then((data) => {
    console.log(data)
    const articles = data.articles; 
    container.innerHTML = "";
    
    let articlesFiltered = articles.filter(item => item.publishedAt.includes(date));
    if (data.articles && data.articles.length > 0) {
      for (let i = 0; i < data.articles.length; i++) {
        const article = data.articles[i];
        const getArticle = document.createElement('div');
        getArticle.setAttribute('id', 'article');
        getArticle.setAttribute('class', 'card');

        const title = document.createElement('h3');
        title.classList.add("title")
        const content = document.createElement('p');
        content.classList.add("content")
        const img = document.createElement('img');
        const dateElement = document.createElement('p')

        const button = document.createElement('button');
        button.setAttribute('class', "card-button")
        button.innerText = 'Videofy'
        dateElement.setAttribute('class', 'date')

        title.innerText = article.title;
        dateElement.innerText = `Published On: ${article.publishedAt}`
        content.innerText = article.content;
        img.setAttribute('src', article.image);
        img.setAttribute('style', 'width: 200px; height: 150px; padding-top:20px; padding-bottom:20px;');

        getArticle.append(title);
        getArticle.append(img);
        getArticle.append(content);
        getArticle.append(button);
        getArticle.append(dateElement)

        getArticle.addEventListener("click", () => {
          let title = document.getElementsByClassName("title")[i]
          let content = document.getElementsByClassName("content")[i]
          // genpromptandspeech(title.innerText,content.innerText)
        });

        container.append(getArticle);
      }
    } else {
      console.log('No articles found for the specified category and date.');
    }
  })
  .catch(error => {
    console.error('Error fetching news:', error);
  });
}


  
  let searchResult = document.getElementById("result")
  let searchInput = document.getElementById("input")


// const listOfArticles = data.articles;

// listOfArticles.forEach((article) => {
//   const getArticle = document.createElement('div');
//   getArticle.setAttribute('id', 'article');
//   getArticle.setAttribute('class', 'article');

//   const title = document.createElement('h3');
//   const content = document.createElement('p');
//   const img = document.createElement('img');

//   title.innerText = article.title;  
//   content.innerText = article.content;
//   img.setAttribute('src', article.image);

//   getArticle.append(title);
//   getArticle.append(img);
//   getArticle.append(content);

//   arr.push(getArticle);
// });

// arr.forEach((ele) => {
//   container.append(ele);
// });



// // Translation


// // searchResult.addEventListner("click", translate())

// function translate() {
//   let input = searchInput.value
//   let language = language.value
  
// }





// -----------------------------------------------------------------------------------------------

async function translateText(textToTranslate,targetLanguage) { 

  try {
    const response = await fetch('http://127.0.0.1:5000/translate_text', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        to_translate: textToTranslate,
        target_language: targetLanguage,
      }),
    });

    const result = await response.json();
    return;
  } catch (error) {
    console.error('Fetch Error:', error);
  }
}

// translateText();


async function imageGenerate(prompt) {
  // const prompt = "Fashion fans rushing to buy 'perfect for work' £30 Amazon handbag that looks just like £1,200 designer Burberry version"

  try {
    const response = await fetch('http://127.0.0.1:5000/generate_image', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        prompt:prompt
      }),
    });

    const result = await response.json();
    console.log(result.result)
  } catch (error) {
    console.error('Fetch Error:', error);
  }
}

// imageGenerate()

async function videoGenerator() {
  const data = {
    images: ['assets/image_0.jpg', 'assets/image_1.jpg','assets/image_2.jpg','assets/image_3.jpg','assets/image_4.jpg'],
    audio: 'assets/output.mp3',
  };

  const options = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  };

  try {
    const response = await fetch('http://127.0.0.1:5000/generate_video', options);
    const result = await response.json();

    console.log(result);
  } catch (error) {
    console.error(error);
  }
}

// videoGenerator()