import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

console.log(import.meta.env.VITE_BACKEND_API)

export const apiSlice = createApi({
    reducerPath: 'backendApi',

    baseQuery: fetchBaseQuery({
        baseUrl: import.meta.env.VITE_BACKEND_API,
        credentials: 'include',
        prepareHeaders: async (headers, { }) => {
            return headers;
        },
    }),
    endpoints: (builder) => ({
        upload: builder.mutation({
            query: ({ formData }) => ({
                url: '/upload',
                method: 'POST',
                body: formData,
            }),
        }),
        download: builder.mutation({
            query: () => ({
                url: '/download_json',
                method: 'GET',
            }),
        })
    })
})

export const {
    useUploadMutation,
    useDownloadMutation,
} = apiSlice;