// 面经相关的请求，放到这个文件中

import request from '@/utils/request'

// 1. 分页获取面经列表数据
// export const ArticleListAPI = params => {
//   return request.get('/admin/interview/query', { params })
// }
export const ArticleListAPI = params => {
  return request({
    url: '/admin/interview/query',
    params
  })
}

// 2. 添加面经
export const addArticleAPI = data => {
  return request.post('/admin/interview/create', data)
}

// 3. 删除面经
export const deleteArticleAPI = id => {
  // return request.delete('/admin/interview/remove', { data: { id } })
  return request({
    method: 'DELETE',
    url: '/admin/interview/remove',
    data: { id }
  })
}

// 4. 获取单个面经详情信息
export const articleAPI = id => {
  return request({
    url: '/admin/interview/show',
    params: { id }
  })
}

// 5. 修改面经
export const updateArticleAPI = data => {
  return request({
    method: 'PUT',
    url: '/admin/interview/update',
    data: data
  })
}
