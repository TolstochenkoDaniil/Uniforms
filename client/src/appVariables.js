export const axiosDefaultsBaseURL = 
    process.env.NODE_ENV === "prodiction"
        ? "https://uniforms.edu"
        : "http://127.0.0.1:8000";
export const axios_defaults_baseFrontURL =
    process.env.NODE_ENV === "production"
        ? "https://uniforms.edu"
        : "http://localhost:8081";
        
export const clientKey = "6eJ4sDQu5vQrg_NpD5tscsGL";
export const oauthGoogle = "407776762528-rm4g0c269q7r57tjaml1qrbqfarot1cp.apps.googleusercontent.com";