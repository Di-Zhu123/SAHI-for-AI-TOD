from sahi.scripts.slice_coco import slice

image_dir='/media/judy/8AAAE75DAAE743F3/AITOD/val/images'
dataset_json_path='/media/judy/8AAAE75DAAE743F3/AITOD/annotations/aitod_val_v1.json'
output_dir='/media/judy/8AAAE75DAAE743F3/AITOD/val/sliced'
slice_size=64
overlap_ratio=0.25

slice(
    image_dir=image_dir,
    dataset_json_path=dataset_json_path,
    ignore_negative_samples= False,
    output_dir=output_dir,
    slice_size=slice_size,
    overlap_ratio=overlap_ratio,
)