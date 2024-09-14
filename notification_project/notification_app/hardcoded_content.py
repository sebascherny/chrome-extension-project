HILTON_URL = "www.hilton.com"
FLYTAP_URL = "www.flytap.com"
FCTGL_URL = "www.fctgl.com"

LIST_OF_URLS = [
    HILTON_URL,
    FLYTAP_URL,
    FCTGL_URL,
]

NOTIFICATION_CONTENT = {
    HILTON_URL: """
        <div>
            <div style="display: flex;">
                <img width=40px height=40px src="https://cdn-icons-png.flaticon.com/512/4885/4885933.png"></img>
                <h1 style="align-self: center;">Should you be here?</h1>
            </div>
            <p>Unless it's a personal trip, then it's really none of our business.</p>
            <p style="font-size: 60%">Leave a comment?</p>
            <input id="comment_input_in_notification" style="margin-bottom: 20px; border: 1px solid black;"></input>
        </div>    
        <button id="dismiss-btn">IT'S A PERSONAL TRIP</button>
        <button id="acknowledge-btn">GO TO FCM HUB</button>
""",
    FLYTAP_URL: """
    <div>
        <h1>Planning on flying??</h1>
        <div style="display: flex; position: absolute; bottom: 20px;">
            <button id="acknowledge-btn" style="margin-right: 20px;">OK</button>
            <button id="dismiss-btn" style="margin-right: 20px;">Bye</button>
        </div>
    </div>""",
    FCTGL_URL: """
        <div style="text-align: center;">
            <h3 style="color: red">FCGTL</h3>
            <p>Do you want to explore flght options?</p>
        </div>
""",
}
