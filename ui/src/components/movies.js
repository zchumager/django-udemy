import React from "react"
import gql from 'graphql-tag'
import {useQuery} from '@apollo/react-hooks'

const GET_MOVIES = gql`
    {
        allMovies {
            id
            title
            year
            director{
              name
              surname
            }
        }
    }
`

function Movies() {

    const {loading, error, data} = useQuery(GET_MOVIES)

    if (loading) return "LOADING DATA"
    if (error) return `ERROR MSG: ${error.message}`

    const movies = data.allMovies

    return (
        <div>
            <h1>List of Movies</h1>
            <ul>
                { movies.map(movie => <li key={movie.id}>{movie.title} ({movie.year})</li>) }
            </ul>
        </div>
    );
}

export default Movies