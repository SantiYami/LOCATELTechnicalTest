export const URI = process.env.VUE_APP_URI

export const SERVICE_NAMES ={
    USER: 'user',
    PRODUCT: 'product',
    SALE_HEADER: 'sale-header',
    SALE_DETAIL: 'sale-detail',
}

export const HTTP_STATUS = {
    OK: 200,
    NO_CONTENT: 204,
    BAD_REQUEST: 400,
    UNAUTHORIZED: 401,
    FORBIDDEN: 403,
    CONFLICT: 409,
    UNPROCESSABLE_ENTITY: 422,
    INTERNAL_SERVER_ERROR: 500,
}