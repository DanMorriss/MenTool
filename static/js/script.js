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