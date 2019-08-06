// Load App's css (scss)
import '@/assets/css/app.scss'

// Import bootstrap js
import 'bootstrap/dist/js/bootstrap.bundle.min'

// Load project image
// import projectImage from '@/assets/images/mws-profile.png'

// // Let's append the image to the page
// const main = document.getElementById('app')
// const image = document.createElement('img')
// image.setAttribute('src', projectImage)
// main.appendChild(image)
//
// // Make a button and attach an async await call to test.
// const button = document.createElement('button')
// button.innerHTML = 'Emulate async/await call'
// button.className = 'main-button'
// main.appendChild(button)
//
// const pinkyPromise = () => {
//     return new Promise((resolve) => {
//         setTimeout(() => {
//             resolve('I pinky promise!')
//         }, 2000)
//     })
// }
//
// button.addEventListener('click', async () => {
//     button.innerHTML = 'Wait a few seconds...'
//     const result = await pinkyPromise()
//     window.alert(result)
//     button.innerHTML = 'Emulate async/await call'
// })
//
// // Make a link to this project's github
// const div = document.createElement('div')
// const link = document.createElement('a')
// link.setAttribute('href', 'https://github.com/johndatserakis/modern-webpack-starter')
// link.innerHTML = 'View on GitHub'
// div.appendChild(

const url = 'http://127.0.0.1:3001/course/api/?format=json'

$(document).ready(function () {

    $.get(url, function (courses, status) {
        courses.forEach(function (course) {
            console.log(course);
            $('#app').append('<div>' + course.title + ' <br>' + course.description + '</div>');
        })

    });
});
