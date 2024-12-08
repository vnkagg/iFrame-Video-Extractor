chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "extractIframe") {
        const iframes = document.querySelectorAll('iframe');
        if (iframes.length > 0) {
            const iframeLinks = Array.from(iframes).map(iframe => iframe.src);
            sendResponse({ iframeLinks });
        } else {
            sendResponse({ iframeLinks: [] });
        }
    }
});
