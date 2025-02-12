import itertools


def calculate_mrr(predictions: list[str], gt: list[str]):
    mrr = 0
    for label in gt:
        if label in predictions:
            # Find the relevant item that has the smallest index
            mrr = max(mrr, 1 / (predictions.index(label) + 1))
    return mrr


def calculate_recall(predictions: list[str], gt: list[str]):
    # Calculate the proportion of relevant items that were retrieved
    return len([label for label in gt if label in predictions]) / len(gt)


def calculate_precision(predictions: list[str], gt: list[str]):
    # Calculate the proportion of retrieved items that are relevant
    return len([label for label in predictions if label in gt]) / len(predictions)


def get_metrics_at_k(
    metrics: list[str],
    sizes: list[int],
):
    metric_to_score_fn = {
        "mrr": calculate_mrr,
        "recall": calculate_recall,
    }

    for metric in metrics:
        if metric not in metric_to_score_fn:
            raise ValueError(f"Metric {metric} not supported")

    eval_metrics = [(metric, metric_to_score_fn[metric]) for metric in metrics]

    return {
        f"{metric_name}@{size}": lambda predictions, gt, m=metric_fn, s=size: (
            lambda p, g: m(p[:s], g)
        )(predictions, gt)
        for (metric_name, metric_fn), size in itertools.product(eval_metrics, sizes)
    }
