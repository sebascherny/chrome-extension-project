// Listens for updates to the active tab
chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.status === 'complete' && tab.active) {
        // Check if the URL matches any of the specified websites
        const allowedWebsites = [
            'https://www.hilton.com',
            'https://www.flytap.com',
            'https://www.fctgl.com'
        ];

        const currentUrl = new URL(tab.url);
        if (allowedWebsites.includes(currentUrl.origin)) {
            // Inject the content script into the active tab
            chrome.scripting.insertCSS({
                target: { tabId: tabId },
                files: ["style.css"]
            }, () => {
                // console.log('CSS injected into tab:', tab.url);
            });
            chrome.scripting.executeScript({
                target: { tabId: tabId },
                files: ['content.js']
            }, () => {
                // console.log('Content script injected into tab:', tab.url);
            });
        }
    }
});
