console.log("RUNNING content.js script");

// Function to notify backend of user interactions
function notifyBackend(action) {
    let comment = '';
    // input's id could come from the backend
    if (document.getElementById("comment_input_in_notification")) {
        comment = document.getElementById("comment_input_in_notification").value;
    }
    fetch('http://127.0.0.1:8001/log-event/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            action: action,
            url: window.location.href,
            comment
        })
    }).then(response => {
        if (!response.ok) {
            console.error('Failed to log event:', action);
        }
    }).catch(error => {
        console.error('Error logging event:', error);
    });
}

function remove_notification_divs() {
    document.getElementById('custom-notification').remove();
    return;
    const notificationElements = document.getElementsByClassName('custom-notification');
    console.log(notificationElements);
    const l = notificationElements.length
    console.log(l);
    for (var i = l - 1; i >= 0; i--) {
        console.log(i);
        console.log(notificationElements[i]);
        notificationElements[i].remove();
        console.log("removed");
    }
}

function acknowledge_click() {
    notifyBackend('acknowledged');
    // remove_notification_divs();
    window.open("http://www.fcm.com/", "_blank");
}

window.byebye = dismiss_click;
document.byebye2 = dismiss_click;

function dismiss_click() {
    notifyBackend('dismissed');
    remove_notification_divs();
}

function displayNotification(content) {
    if (document.getElementById('custom-notification')) {
        console.log("Avoiding duplicate notifications"); // Could remove it and create a new if context is important
        return;
    }
    const notificationDiv = document.createElement('div');
    notificationDiv.id = 'custom-notification';
    notificationDiv.innerHTML = `<div>${content}</div>`;
    const dismissButton = document.createElement('button');
    dismissButton.id = 'dismiss-btn';
    dismissButton.innerHTML = "IT'S A PERSONAL TRIP";
    dismissButton.onclick = dismiss_click;
    notificationDiv.appendChild(dismissButton);
    const acknowledgeButton = document.createElement('button');
    acknowledgeButton.id = 'acknowledge-btn';
    acknowledgeButton.innerHTML = "GO TO FCM HUB";
    acknowledgeButton.onclick = acknowledge_click;
    notificationDiv.appendChild(acknowledgeButton);
    const closeButton = document.createElement('button');
    closeButton.id = 'close-notif-btn';
    closeButton.className = 'close-btn';
    closeButton.innerHTML = "X";
    closeButton.onclick = dismiss_click;
    notificationDiv.appendChild(closeButton);
    document.body.appendChild(notificationDiv);
    // Notify backend that the notification has been displayed
    notifyBackend('displayed');
}

// Check if the extension is active on the current site
if (window.location.hostname === 'www.hilton.com' || window.location.hostname === 'www.flytap.com' || window.location.hostname === 'www.fctgl.com') {
    // Fetch content from the backend API
    fetch('http://127.0.0.1:8001/get-notification/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            url: window.location.href
        })
    })
        .then(response => response.text())
        .then(data => {
            // Display the notification with the fetched content
            displayNotification(data);
        })
        .catch(error => {
            console.error('Error fetching notification:', error);
        });
}
