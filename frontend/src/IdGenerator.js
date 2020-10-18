export default {
  // Convert a URL into an html id. This is a workaround for bootstrap modal.
  // It has difficulties when the id of an element has the same format as an url.
  fromURL (url, prefix = '') {
    const regex = /:|\/|\.|\?|#|=/gm
    const subst = '-'
    return `${prefix}-${url.replace(regex, subst)}`
  }
}
