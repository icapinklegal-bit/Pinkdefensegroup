def P(path, title, desc, body='', levels=None, faq=None, kind='criminal', hub=False, cat=None, **kw):
    d = dict(path=path, title=title, desc=desc, body=body, kind=kind, hub=hub,
             cat=cat or path.split('/')[0])
    if levels: d['levels'] = levels
    if faq: d['faq'] = faq
    d.update(kw)
    return d
