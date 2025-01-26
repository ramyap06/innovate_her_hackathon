from flask import Flask, render_template, request, jsonify
import ipinfo

name = ['Amelia Earhart', 'Winifred Parker', 'Frieda Parker', 'Virginia C Meredith', 'Mari Evans', 'Eva Mozes Kor', 'Madam CJ Walker', 'Frances Morgan Swain']
lat = [40.42553, 40.427836, 40.428478, 40.426429, 39.773611, 39.450220, 39.776150, 39.167125]
long = [-86.92514, -86.920856, -86.919540, -86.923241, -86.151306, -87.413290, -86.167213, -86.525428]
description = ['Amelia Mary Earhart, born July 24, 1897, was an American aviation pioneer. On July 2, 1937, she disappeared over the Pacific Ocean while attempting to become the first female pilot to circumnavigate the world. During her life, Earhart embraced celebrity culture and women\'s rights, and since her disappearance has become a global cultural figure. She was the first female pilot to fly solo non-stop across the Atlantic Ocean and set many other records.', 
                        'During the early stages of the American civil rights movement and well before the landmark Brown v. Board of Education decision, sisters Winifred and Frieda Parker were leading the effort to integrate student housing on Purdue\'s campus and across Indiana. On Oct. 3, the Parker sisters were honored for their courageous leadership with the dedication of two residence halls in their names on the Purdue University campus.',
                        'During the early stages of the American civil rights movement and well before the landmark Brown v. Board of Education decision, sisters Winifred and Frieda Parker were leading the effort to integrate student housing on Purdue\'s campus and across Indiana. On Oct. 3, the Parker sisters were honored for their courageous leadership with the dedication of two residence halls in their names on the Purdue University campus.',
                        'Born in 1848, Virginia Claypool Meredith, married Henry C. Meredith in 1870. Henry died in 1882 at the age of 37, leaving Virginia a 33-year-old widow.She continued on at the Oakland farm and raised prize winning Shorthorn cattle and Southdown sheep. She had hired help on the farm, but her meticulous records on all breeding and sales made her the successful woman rancher she became. Meredith Hall, a women\'s residence hall, was named in Virginia\'s honor. Her legacy was quite far flung and women on campus today owe much to Virginia\'s ability to advocate on their behalf.',
                        'Mari Evans was born in Toledo, Ohio, in 1923. She moved to Indianapolis in 1947 and became a prominent figure in the Black Arts Movement. She was a poet, playwright, and children\'s book author. Evans was a writer-in-residence at Indiana University-Purdue University Indianapolis and was a visiting professor at Cornell University. She was also a writer-in-residence at the University of Miami. Evans was a member of the American Academy of Poets and the American Academy of Arts and Letters. She was the recipient of the Indiana Governor\'s Arts Award and the Madam C.J. Walker Award.',
                        'A Holocaust survivor, Eva Mozes Kor and her twin sister were subjected to horrific human experimentation at Auschwitz. Kor was an activist, author and founder of CANDLES (Children of Auschwitz Nazi Deadly Lab Experiments Survivors), an organization devoted to educating the public about eugenics, the Holocaust, and the power of forgiveness. Kor was a long-time resident of Terre Haute.',
                        'Madam CJ Walker was a Black entrepreneur, philanthropist and activist. Madam Walker was the first self-made woman millionaire, as documented by Guinness World Records. She founded Madam CJ Walker Manufacturing Company which developed hair care products. The manufacturing headquarters was repurposed and is now named The Madam Walker Legacy Center, it stands as a testament to Madam Walker\'s entrepreneurial spirit.',
                        'Nearly two decades before women won the right to vote, Frances Morgan Swain, wife of Joseph Swain IU\'s ninth president, was lobbying IU\'s trustees for a space devoted to female students on campus. Now, more than 100 years later, the space she helped build will bear her name.']


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Your HTML file

#@app.route('/get-sites', methods=['POST'])
@app.route('/get-location')
def get_location():
    access_token = "a0a64e2001c43d"
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails()
    location = details.loc

    latitude = float(location.split(",")[0])
    longitude = float(location.split(",")[1])

    return jsonify({"latitude": latitude, "longitude": longitude})
'''
    link = ['https://www.google.com/maps/dir/?api=1&origin=' + latitude + "," + longitude + '&destination=40.42553,-86.92514&travelmode=driving',
            'https://www.google.com/maps/dir/?api=1&origin=' + latitude + "," + longitude + '&destination=40.427836,-86.920856&travelmode=driving',
            'https://www.google.com/maps/dir/?api=1&origin=' + latitude + "," + longitude + '&destination=40.428478,-86.919540&travelmode=driving',
            'https://www.google.com/maps/dir/?api=1&origin=' + latitude + "," + longitude + '&destination=40.426429,-86.923241&travelmode=driving',
            'https://www.google.com/maps/dir/?api=1&origin=' + latitude + "," + longitude + '&destination=39.773611,-86.151306&travelmode=driving',
            'https://www.google.com/maps/dir/?api=1&origin=' + latitude + "," + longitude + '&destination=39.450220,-87.413290&travelmode=driving',
            'https://www.google.com/maps/dir/?api=1&origin=' + latitude + "," + longitude + '&destination=39.776150,-86.167213&travelmode=driving',
            'https://www.google.com/maps/dir/?api=1&origin=' + latitude + "," + longitude + '&destination=39.167125,-86.525428&travelmode=driving']
'''
    
'''
    sites = []
    for i in range(8):
        distance = ((lat[i] - latitude) ** 2) + ((long[i] - longitude) ** 2)
        if distance <= 10:
            sites.append([name[i], description[i], lat[i], long[i]])
'''
    
@app.route('/set-sites')
def set_sites():
    sites = []
    for i in range(8):
        distance = ((lat[i] - latitude) ** 2) + ((long[i] - longitude) ** 2)
        if distance <= 10:
            sites.append([name[i], description[i], lat[i], long[i]])

if __name__ == '__main__':
    app.run(debug=True)