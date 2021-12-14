# utility functions for making plots

def set_plot_params(ax,xticks,yticks,
                    xlabel,ylabel,x_sciformat = 1,y_sciformat = 1):
    plt.tick_params(direction = 'in',top = True,right = True,left = True,bottom = True, length = 6)


    if x_sciformat != 1 or y_sciformat != 1:
        xticklabels = np.array(xticks)/x_sciformat
        yticklabels = np.array(yticks)/y_sciformat
        
    else:
        xticklabels = xticks
        yticklabels = yticks
        
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels,fontsize = 15)

    ax.set_yticks(yticks)
    ax.set_yticklabels(yticklabels,fontsize = 15)

    ax.set_xlabel(xlabel,fontsize = 18)
    ax.set_ylabel(ylabel,fontsize = 18)

