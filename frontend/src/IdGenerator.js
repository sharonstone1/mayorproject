export default {
  fromURL (url, prefix = '') {
    const regex = /:|\/|\.|\?|#|=/gm
    const subst = '-'
    return `${prefix}-${url.replace(regex, subst)}`
  }
}
