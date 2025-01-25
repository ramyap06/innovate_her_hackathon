import pandas as pd

data = {'Name': ['Amelia Earhart', 'Winifred Parker', 'Frieda Parker', 'Virginia C Meredith'], 
        'Lat': [40.42553, 40.427836, 40.428478, 40.426429], 
        'Long': [-86.92514, -86.920856, -86.919540, -86.923241], 
        'Description': ['Amelia Mary Earhart, born July 24, 1897, was an American aviation pioneer.' 
                        +' On July 2, 1937, she disappeared over the Pacific Ocean while attempting to'
                        + 'become the first female pilot to circumnavigate the world. During her life,'
                        + 'Earhart embraced celebrity culture and women\'s rights, and since her disappearance'
                        + 'has become a global cultural figure. She was the first female pilot to fly'
                        + 'solo non-stop across the Atlantic Ocean and set many other records.', 
                        'During the early stages of the American civil rights movement and well before' 
                        + 'the landmark Brown v. Board of Education decision, sisters Winifred and Frieda Parker were' 
                        + 'leading the effort to integrate student housing on Purdue\'s campus and across Indiana.' 
                        + 'On Oct. 3, the Parker sisters were honored for their courageous leadership with the' 
                        + 'dedication of two residence halls in their names on the Purdue University campus.',
                        'During the early stages of the American civil rights movement and well before' 
                        + 'the landmark Brown v. Board of Education decision, sisters Winifred and Frieda Parker were' 
                        + 'leading the effort to integrate student housing on Purdue\'s campus and across Indiana.' 
                        + 'On Oct. 3, the Parker sisters were honored for their courageous leadership with the' 
                        + 'dedication of two residence halls in their names on the Purdue University campus.',
                        'Born in 1848, Virginia Claypool Meredith, married Henry C. Meredith in 1870. Henry died in 1882 at the age of 37, leaving Virginia a 33-year-old widow.She continued on at the Oakland farm and raised prize winning Shorthorn cattle and Southdown sheep. She had hired help on the farm, but her meticulous records on all breeding and sales made her the successful woman rancher she became. Meredith Hall, a women\'s residence hall, was named in Virginia\'s honor. Her legacy was quite far flung and women on campus today owe much to Virginia\'s ability to advocate on their behalf.'
                        ]
                        }
df = pd.DataFrame(data)