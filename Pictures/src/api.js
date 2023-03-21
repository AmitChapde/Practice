import axios from 'axios';


const searchImages= async (term) =>{
    const response= await axios.get('https://api.unsplash.com/search/photos',{
        headers :{
            Authorization:'Client-ID xONeDu2fsfd0zvSRVmSuU6P4ulEjn8WJMYB68piBQKM'
        },
        params:{
            query:term,
        }
    });

    
    return response.data.results;
};

export default searchImages;