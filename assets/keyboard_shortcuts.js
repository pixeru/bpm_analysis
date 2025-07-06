// assets/keyboard_shortcuts.js

// This ensures the clientside namespace is available
window.dash_clientside = window.dash_clientside || {};

// Define a namespace for our keyboard functions
window.dash_clientside.keyboard = {
    // This is the function we will call from Python
    // The function should return the data to be stored in the keyboard-store
    setup_hotkeys: function(pathname) {
        // We add a flag to the window object to ensure this listener is only added once
        if (window.hotkeyListenerAttached) {
            return null; // Return null to indicate no update needed
        }

        const handler = (e) => {
            const key = e.key.toLowerCase();

            // Prevents shortcuts from firing when you're typing in an input field
            if (e.target.tagName === 'INPUT') {
                return;
            }

            // Check for 'z' or 'x' and update the store directly
            if (key === 'z' || key === 'x') {
                // Store the key data in a global variable that can be accessed by the callback
                window.lastKeyPressed = { last_key: key, timestamp: Date.now() };
                
                // Trigger a custom event to notify that data has changed
                const event = new CustomEvent('keyboardDataChanged');
                document.dispatchEvent(event);
            }
        };

        document.addEventListener('keydown', handler);
        window.hotkeyListenerAttached = true; // Set the flag
        
        // Return initial data (empty) to complete the callback
        return { last_key: null, timestamp: null };
    },

    // Function to check for new keyboard data
    check_keyboard_data: function(n_intervals) {
        // Check if there's new keyboard data
        if (window.lastKeyPressed) {
            const newData = window.lastKeyPressed;
            window.lastKeyPressed = null; // Clear the data
            return newData;
        }
        
        // Return null if no new data (no update needed)
        return null;
    },

    // Combined function that handles both setup and periodic checking
    handle_keyboard_combined: function(pathname, n_intervals) {
        // If this is the first call (pathname changed), set up the keyboard listener
        if (!window.hotkeyListenerAttached) {
            const handler = (e) => {
                const key = e.key.toLowerCase();

                // Prevents shortcuts from firing when you're typing in an input field
                if (e.target.tagName === 'INPUT') {
                    return;
                }

                // Check for 'z' or 'x' and store the data
                if (key === 'z' || key === 'x') {
                    window.lastKeyPressed = { last_key: key, timestamp: Date.now() };
                }
            };

            document.addEventListener('keydown', handler);
            window.hotkeyListenerAttached = true;
            
            // Return initial data
            return { last_key: null, timestamp: null };
        }
        
        // For subsequent calls (interval triggered), check for new keyboard data
        if (window.lastKeyPressed) {
            const newData = window.lastKeyPressed;
            window.lastKeyPressed = null; // Clear the data
            return newData;
        }
        
        // Return null if no new data (no update needed)
        return null;
    }
};