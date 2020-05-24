class Document:
    all_files = {}
    def __init__(this,file_name,author,shareable=False):
        this.file_name = file_name
        this.author = author
        this.shareable = shareable
        this.editors = []
        this.viewers = []
        this.count=0
        files[file_name]=this

    def toggle_visibilty(this):
        this.shareable = not this.shareable

    
