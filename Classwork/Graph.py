from calendar import error


class Graph:
    def __init__(self,directed=False):
        self.directed= directed
        self.adj_list= dict()
    def bfs(self):
        pass
    def dfs(self):
        pass
    def __repr__(self):
        str_graph = ""
        for key, value in self.adj_list.items():
            str_graph += f"{key} -> {value}"
        return str_graph
    def add_node(self,node):
        if node not in self.adj_list:
            self.adj_list[node]=set()
        else:
            raise ValueError("Node already exists")

    def add_edge(self,source,dest,weighted = None):
        if source not in self.adj_list:
            self.add_node(source)
        if dest not in self.adj_list:
            self.add_node(dest)
        if weighted is None:
            self.adj_list[source].add(dest)
            if self.directed:
                self.adj_list[dest].add(source)
        else:
            self.adj_list[source].add((dest,weighted))
            if self.directed:
                self.adj_list[dest].add((source, weighted))

    def adj_matrix(self):
        pass

    def obtain_neighbor(self,node):
        return self.adj_list

if __name__ == '__main__':
    graphobj= Graph()