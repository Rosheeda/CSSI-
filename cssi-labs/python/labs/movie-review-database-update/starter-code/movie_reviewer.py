#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

inside_movie = {
    "title": "Inside Out",
    "id": "tt2096673",
    "year_released": 2012,
    "rating": "PG",
    "score": 7.5,
    "out_of": 10,
    "reviews": 463787
}

# Do not edit the code above!

# Write your code below to update the information in accordance with its
# IMDB page: http://www.imdb.com/title/tt2096673/
inside_movie["year_released"] = 2015
inside_movie["score"] = 8.2
inside_movie["reviews"] = 492446

#removing key out_of
inside_movie.pop("out_of")

#adding new key/value pair to dictionary
inside_movie["genre"] = [ "Animation", "Adventure", "Comedy" ]

#printing key/values
for i in inside_movie:
    print i, ":",inside_movie[i]

shrek_movie = {
    "title": "Shrek",
    "id": "tt0126029",
    "year_released": 2001,
    "rating": "PG",
    "score": 7.9,
    "reviews": 531432,
    "genre": [ "Animation", "Adventure", "Comedy" ]
}

for i,j in shrek_movie.items():
    print i, ":",j

movies = [shrek_movie, inside_movie]

user = raw_input("Enter a genre: ").capitalize()

bestMovie = {"title":"none","score":0}

for i in movies:
    if user in i["genre"]:
        if bestMovie["rating"] < i["rating"]:
            bestMovie["rating"] = i["rating"]
            bestMovie["title"] = i["title"]

print bestMovie["title"]
