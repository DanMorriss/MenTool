// fade the alert messages

function fadeOutAlert() {
   const alerts = document.querySelectorAll('.alert');

   alerts.forEach((alert) => {
       setTimeout(() => {
           alert.style.transition = 'opacity 1s';
           alert.style.opacity = '0';

           setTimeout(() => {
               alert.remove();
           }, 1000); // Remove the alert after fade out
       }, 3000); // Delay for 3 seconds before starting to fade out
   });
}

window.addEventListener('load', fadeOutAlert);

// retrieve the user's information from GitHub and LinkedIn 
 
function userInformationHTML(user) {
   return `
   <h2>${user.name}
       <span class="small-name">
           (@<a href="${user.html_url}" target="_blank">${user.login}</a>)
       </span>
   </h2>
   <div class="gh-content">
       <div class="gh-avatar">
           <a href="${user.html_url}" target="_blank">
               <img src="${user.avatar_url}" width="80" height="80" alt="${user.login}" />
           </a>
       </div>
       <p>Followers: ${user.followers} - Following ${user.following} <br> Repos: ${user.public_repos}</p>
   </div>`;
}

function repoInformationHTML(repos) {
   if (repos.length == 0) {
       return `<div class="clearfix repo-list">No repos!</div>`;
   }

   var listItemsHTML = repos.map(function (repo) {
       return `<li>
               <a href="${repo.html_url}" target="_blank">${repo.name}</a>
           </li>`;
   });

   return `<div class="clearfix repo-list">
           <p>
               <strong>Repo List:</strong>
           </p>
           <ul>
               ${listItemsHTML.join("\n")}
           </ul>
       </div>`;
}

function fetchGitHubInformation(event) {
   $("#gh-user-data").html("");
   $("#gh-repo-data").html("");

   var username = $("#gh-username").val();
   if (!username) {
       $("#gh-user-data").html(`<h2>Please enter a GitHub username</h2>`);
       return;
   }

   $.when(
       $.getJSON(`https://api.github.com/users/${username}`),
       $.getJSON(`https://api.github.com/users/${username}/repos`)
   ).then(
       function (firstResponse, secondResponse) {
           var userData = firstResponse[0];
           var repoData = secondResponse[0];
           $("#gh-user-data").html(userInformationHTML(userData));
       },
       function (errorResponse) {
           if (errorResponse.status === 404) {
               $("#gh-user-data").html(
                   `<h2>No info found for user ${username}</h2>`);
           } else {
               console.log(errorResponse);
               $("#gh-user-data").html(
                   `<h2>Error: ${errorResponse.responseJSON.message}</h2>`);
           }
       });
}

$(document).ready(fetchGitHubInformation);

