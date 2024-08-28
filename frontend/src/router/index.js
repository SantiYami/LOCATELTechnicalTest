import Vue from 'vue'
import VueRouter from 'vue-router'
const HomeView = () => import('../components/views/HomeView.vue')
const CreateClient = () => import('../components/views/ClientCreate.vue')
const CreateProduct = () => import('../components/views/ProductCreate.vue')
const CreateSaleHeader = () => import('../components/views/SaleHeaderCreate.vue')
const CreateSaleDetail = () => import('../components/views/SaleDetailCreate.vue')
const LoginView = () => import('../components/views/LoginView.vue')
const NotFound = () => import('../components/shared/NotFound.vue')

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  { 
    path: '/create-client',
    name: 'create-client',
    component: CreateClient
  },
  { 
    path: '/create-product',
    name: 'create-product',
    component: CreateProduct
  },
  { 
    path: '/create-sale-header',
    name: 'create-sale-header',
    component: CreateSaleHeader
  },
  { 
    path: '/create-sale-detail',
    name: 'create-sale-detail',
    component: CreateSaleDetail
  },
  {
    // path: "*",
    path: "/:catchAll(.*)",
    name: "NotFound",
    component: NotFound,
  } 
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
