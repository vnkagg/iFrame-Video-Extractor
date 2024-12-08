chrome.action.onClicked.addListener((tab) => {
    chrome.scripting.executeScript(
        {
            target: { tabId: tab.id },
            files: ["content.js"]
        },
        () => {
            chrome.tabs.sendMessage(tab.id, { action: "extractIframe" }, (response) => {
                if (response && response.iframeLinks.length > 0) {
                    response.iframeLinks.forEach(link => {
                        if (link != "about:blank" && link != ""){
                            console.log("Found iframe link:", link);
                            const port = chrome.runtime.connectNative('com.az.iframe.bridge')
                            port.onMessage.addListener((message) => {
                                console.log('Received from host:', message);
                                port.disconnect();
                            });
                            
                            port.onDisconnect.addListener(() => {
                                console.log('Disconnected from native host');
                                if(chrome.runtime.lastError){
                                    console.log('chrome.runtime.lastError: ', chrome.runtime.lastError)
                                    chrome.tabs.create({ url: link });
                                }
                            });
                            port.postMessage({ url : link });
                        }
                        // chrome.runtime.sendNativeMessage(
                        //     "com.az.iframebridge", // Native messaging host name
                        //     { url: link }, // Message payload
                        //     (nativeResponse) => {
                        //         if (chrome.runtime.lastError) {
                        //             console.error("Failed to send message:", chrome.runtime.lastError.message);
                        //         } else {
                        //             console.log("Native host response:", nativeResponse);
                        //         }
                        //     }
                        // );
                    });
                } else {
                    console.log("No iframes found on the page.");
                }
            });
        }
        );
    });

// fetch('http://localhost:6969/run_az_lec', {
//     method: 'POST',
//     headers: { 'Content-Type': 'application/json' },
//     body: JSON.stringify({ link })
// })
// .then(response => response.json())
// .then(data => console.log("Server response:", data));
