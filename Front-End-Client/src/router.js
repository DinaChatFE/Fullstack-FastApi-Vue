import { createWebHistory, createRouter } from "vue-router";
import HomePage from './Page/HomePage'
import LoginPage from './Page/LoginPage'
import RegisterPage from './Page/RegisterPage'
import DetailsPage from './Page/DetailsPage'
import ListPostPage from './Page/ListPostPage'
import ProfilePage from './Page/ProfilePage'
import NotFound from './Page/NotFoundPage'

const routes = [
  {
    path: "/",
    name: "Home",
    component: HomePage,
  },
  {
    path: "/login",
    name: "Login",
    component: LoginPage,
  },
  {
    path: "/register",
    name: "Register",
    component: RegisterPage,
  },
  {
    path: "/detail/:path/:id",
    name: "Details",
    component: DetailsPage

  },
  {
    path: "/news",
    name: "News",
    component: ListPostPage

  },
  {
    path: "/profile",
    name: "Profile",
    component: ProfilePage
  },
  {
    path: "/:catchAll(.*)",
    name: "NotFound",
    component: NotFound
  }
];
const router = createRouter({
  history: createWebHistory(),
  routes,
});

/* var isAuthenticated = true
router.beforeEach((to, from, next) => {
  if (to.name != 'Home' && isAuthenticated) next({ name: 'Login' })
  // if the user is not authenticated, `next` is called twice
  else next()
})
 */



export default router;