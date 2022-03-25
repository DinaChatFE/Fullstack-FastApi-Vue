import { createRouter, createWebHistory } from 'vue-router'
import store from '@/store/store'
import { IS_USER_AUTHENTICATED_GETTER } from "@/store/storeconstants";

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: () => import('@/views/Dashboard.vue'),
    meta: {
      auth: true,
      layout: "LayoutAdmin",
    }
  },
  {
    path: '/user',
    name: 'User All',
    component: () => import('@/views/users/All.vue'),
    meta: {
      auth: true,
      layout: "LayoutAdmin",
    }
  },
  {
    path: '/profile',
    name: 'User Profile',
    component: () => import('@/views/users/Profile.vue'),
    meta: {
      auth: true,
      layout: "LayoutAdmin",
    }
  },
  {
    path: '/create-user',
    name: 'Create User',
    component: () => import('@/views/users/Add.vue'),
    meta: {
      auth: true,
      layout: "LayoutAdmin",
    }
  },
  {
    path: '/user/:id',
    name: 'Edit User',
    component: () => import('@/views/users/Edit.vue'),
    meta: {
      auth: true,
      layout: "LayoutAdmin",
    }
  },
  {
    path: '/event',
    name: 'Event All',
    component: () => import('@/views/events/All.vue'),
    meta: {
      auth: true,
      layout: "LayoutAdmin",
    }
  },
  {
    path: '/create-event',
    name: 'Create Event',
    component: () => import('@/views/events/Add.vue'),
    meta: {
      auth: true,
      layout: "LayoutAdmin",
    }
  },
  {
    path: '/event/:event_id',
    name: 'Edit Event',
    component: () => import('@/views/events/Edit.vue'),
    meta: {
      auth: true,
      layout: "LayoutAdmin",
    }
  },
  {
    path: '/event/:id',
    name: 'Event Show',
    component: () => import('@/views/events/Show.vue'),
    meta: {
      auth: true,
      layout: "LayoutAdmin",
    }
  },
  {
    path: '/category',
    name: 'Category All',
    component: () => import('@/views/categories/All.vue'),
    meta: {
      auth: true,
      layout: "LayoutAdmin",
    }
  },
  {
    path: '/create-category',
    name: 'Create Category',
    component: () => import('@/views/categories/Add.vue'),
    meta: {
      auth: true,
      layout: "LayoutAdmin",
    }
  },
  {
    path: '/category/:id',
    name: 'Edit Category',
    component: () => import('@/views/categories/Edit.vue'),
    meta: {
      auth: true,
      layout: "LayoutAdmin",
    }
  },
  {
    path: '/news',
    name: 'News All',
    component: () => import('@/views/news/All.vue'),
    meta: {
      auth: true,
      layout: "LayoutAdmin",
    }
  },
  {
    path: '/news/:id',
    name: 'News Show',
    component: () => import('@/views/news/Show.vue'),
    meta: {
      auth: true,
      layout: "LayoutAdmin",
    }
  },
  {
    path: '/create-news',
    name: 'Create News',
    component: () => import('@/views/news/Add.vue'),
    meta: {
      auth: true,
      layout: "LayoutAdmin",
    }
  },
  {
    path: '/news/:id',
    name: 'News Edit',
    props: true,
    component: () => import('@/views/news/Edit.vue'),
    meta: {
      auth: true,
      layout: "LayoutAdmin",
    }
  },
  {
    path: '/sign-in',
    name: 'SignIn',
    meta: {
      auth: false,
      layout: "LayoutDefault"
    },
    component: () => import('@/views/Login.vue')
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    meta: {
      auth: false,
      layout: "LayoutDefault"
    },
    component: () => import('@/views/SignUp.vue')
  },
  {
    path: '/:pathMatch(.*)*',
    meta: {
      auth: false
    },
    component: () => import('@/views/404.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if ('auth' in to.meta && to.meta.auth && !store.getters[`auth/${IS_USER_AUTHENTICATED_GETTER}`]) {
    next('/sign-in');
  } else if ('auth' in to.meta && !to.meta.auth && store.getters[`auth/${IS_USER_AUTHENTICATED_GETTER}`]) {
    next('/');
  } else {
    next();
  }
});

export default router
